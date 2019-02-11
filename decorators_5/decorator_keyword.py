def keyword(name=None, tags=(), types=()):
    """Decorator to set custom name, tags and argument types to keywords.
    This decorator creates ``robot_name``, ``robot_tags`` and ``robot_types``
    attributes on the decorated keyword method or function based on the
    provided arguments. Robot Framework checks them to determine the keyword's
    name, tags, and argument types, respectively.
    Name must be given as a string, tags as a list of strings, and types
    either as a dictionary mapping argument names to types or as a list
    (or tuple) of types mapped to arguments based on position. It is OK to
    specify types only to some arguments, and setting ``types`` to ``None``
    disables type conversion altogether.
    Examples::
        @keyword(name='Login Via User Panel')
        def login(username, password):
            # ...
        @keyword(name='Logout Via User Panel', tags=['example', 'tags'])
        def logout():
            # ...
        @keyword(types={'length': int, 'case_insensitive': bool})
        def types_as_dict(length, case_insensitive=False):
            # ...
        @keyword(types=[int, bool])
        def types_as_list(length, case_insensitive=False):
            # ...
        @keyword(types=None])
        def no_conversion(length, case_insensitive=False):
            # ...
    If ``name`` is not given, the actual name of the keyword will not be
    affected, but the ``robot_name`` attribute will still be created.
    This can be useful for marking methods as keywords in a dynamic library.
    In this usage it is possible to also omit parenthesis when using the
    decorator::
        @keyword
        def func():
            # ...
    """
    if callable(name):
        return keyword()(name)
    def decorator(func):
        func.robot_name = name
        func.robot_tags = tags
        func.robot_types = types
        return func
return decorator