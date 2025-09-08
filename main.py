#!/usr/bin/env python3

import json

# import yaml # UNCOMMENT FOR USE WITH YAML
from typing import Any

CLASS_PREFIX = "MyClass"


def helper_recurse(
    d: Any,
    mapping: dict = {},
    counter: int = 0,
    curr_class_name: str = f"{CLASS_PREFIX}0",
    curr_key: str = "",
) -> int:
    if curr_class_name not in mapping:
        mapping[curr_class_name] = {}
    if isinstance(d, dict):
        counter += 1
        new_class_name = f"{CLASS_PREFIX}{counter}"
        if curr_key != "":
            mapping[curr_class_name][curr_key] = new_class_name
        for k, v in d.items():
            counter = helper_recurse(
                d=v,
                mapping=mapping,
                counter=counter,
                curr_class_name=new_class_name,
                curr_key=k,
            )
    elif isinstance(d, list):
        # check elements of list
        if len(d) == 0:
            # raise NotImplementedError("empty lists are not supported for now")
            assert curr_key != ""
            mapping[curr_class_name][
                curr_key
            ] = f"List[Any] = Field(default_factory=list)  # TODO: This is an assumption for empty lists"
        else:
            elem = d[0]
            if isinstance(elem, dict):
                counter += 1
                new_class_name = f"{CLASS_PREFIX}{counter}"
                assert curr_key != ""
                mapping[curr_class_name][curr_key] = f"List[{new_class_name}]"
                counter = helper_recurse(
                    d=v,
                    mapping=mapping,
                    counter=counter,
                    curr_class_name=new_class_name,
                    curr_key="",
                )
            if isinstance(elem, (int, str)):
                elemtype = elem.__class__.__name__
                assert curr_key != ""
                mapping[curr_class_name][curr_key] = f"List[{elemtype}]"
            raise NotImplementedError(f"list elem unsupported type {type(elem)} {elem}")
    elif isinstance(d, str):
        assert curr_key != ""
        mapping[curr_class_name][curr_key] = "str"
    elif isinstance(d, int):
        assert curr_key != ""
        mapping[curr_class_name][curr_key] = "int"
    elif d is None:
        assert curr_key != ""
        mapping[curr_class_name][
            curr_key
        ] = "Optional[Any] = None  # TODO: This is an assumption for None/null"
    else:
        raise NotImplementedError(f"unsupported type {type(d)} {d}")
    return counter


def get_python_code(d: dict) -> str:
    assert isinstance(d, dict)
    flat_classes_mapping = {}
    helper_recurse(d=d, mapping=flat_classes_mapping)
    print("flat_classes_mapping", flat_classes_mapping)
    code = """
#!/usr/bin/env python3

from typing import Any, List, Optional
from pydantic import BaseModel, Field

"""
    class_integers = [
        int(x.removeprefix(CLASS_PREFIX), base=10) if isinstance(x, str) else x
        for x in flat_classes_mapping.keys()
    ]
    class_integers = reversed(sorted(class_integers))
    class_names = [f"{CLASS_PREFIX}{x}" for x in class_integers]
    # for class_name, class_mapping in flat_classes_mapping.items():
    for class_name in class_names:
        class_mapping = flat_classes_mapping[class_name]
        assert isinstance(class_mapping, dict)
        if len(class_mapping) == 0:
            continue
        code += f"\nclass {class_name}(BaseModel):\n"
        for k, v in class_mapping.items():
            code += f"    {k}: {v}\n"
    code += """


def parse_test():
    import json
    # import yaml # UNCOMMENT FOR USE WITH YAML
    with open("input.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        # data = yaml.safe_load(f) # UNCOMMENT FOR USE WITH YAML AND COMMENT ABOVE LINE
    assert isinstance(data, dict)
    my_class_1 = MyClass1.model_validate(data)
    print("my_class_1")
    print(my_class_1)

if __name__ == "__main__":
    parse_test()
"""
    return code


def main():
    with open("input.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        # data = yaml.safe_load(f) # UNCOMMENT FOR USE WITH YAML AND COMMENT ABOVE LINE
    assert isinstance(data, dict)
    code = get_python_code(data)
    print("code")
    print(code)
    with open("output.py", "w", encoding="utf-8") as f:
        f.write(code)


if __name__ == "__main__":
    main()
