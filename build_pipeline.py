def build_pipeline(operation_names):
    operations = {
        "double":lambda x:x*2,
        "triple":lambda x:x*3,
        "square":lambda x:x*x
        }
    for name in operation_names:
        if name not in operations:
            raise KeyError
    def pipeline(x):
        value = x
        for name in operation_names:
            value = operations[name](value)
        return value
    return pipeline