from .compat import lru_cache
from hl7apy.exceptions import ChildNotFound


def _construct_hl7_primitives(ELEMENTS, BASE_DATATYPES):
    @lru_cache(maxsize=None)
    def get(name, element_type):
        try:
            return ELEMENTS[element_type][name]
        except KeyError:
            raise ChildNotFound(name)

    @lru_cache(maxsize=None)
    def find(name, where):
        for cls in where:
            try:
                # # Inlining the function
                # return {'ref': get(name, cls.__name__), 'name': name, 'cls': cls}
                return {'ref': ELEMENTS[cls.__name__][name], 'name': name, 'cls': cls}
            except KeyError:
                pass
        raise ChildNotFound(name)

    def is_base_datatype(datatype):
        return datatype in BASE_DATATYPES

    def get_base_datatypes():
        return BASE_DATATYPES

    return get, find, is_base_datatype, get_base_datatypes
