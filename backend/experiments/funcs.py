
def haha(*values):
    for value in values:
        print(value)


def hoho(x, y=0, **key_values):
    print(f"x={x}, y={y}")
    for key,value in key_values.items():
        print(key, value)

def render_template(content: str, **parameters):

    for param_name, param_value in parameters.items():
        content = content.replace("{{"+param_name+"}}", str(param_value))

    return content

print(render_template("hahaxxx", x=5))

#print("{1} {0} {2} {2}".format(1, 5, "haha"))

#haha(1, 5, "haha", "394875ouhger")

#print("{x} {y} {z}".format(z=1, x=5, y="haha"))

#hoho(1, a=1, b=2)