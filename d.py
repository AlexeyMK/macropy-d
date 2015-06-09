def d(*args, **argv):
  import inspect
  d_name = argv.get('d_name', 'd')
  cur = inspect.currentframe()
  calling_frame = inspect.getouterframes(cur)[1]

  frameinfo = inspect.getframeinfo(calling_frame[0])
  stack = inspect.stack()
  print stack
  import pdb; pdb.set_trace()
  string = frameinfo.code_context[0].strip()
  import ast
  ast_module = ast.parse(string)
  ast_func_call = [node for node in ast.walk(ast_module)
      if node.__class__.__name__ == 'Call' and
         node.func.__dict__.get('id') == d_name]

  if len(ast_func_call) > 1:
      raise ValueError("One contextify per line, please")

  # TODO named arguments
  # TODO give better error when called with something other than variables
  arg_names = [arg.id for arg in ast_func_call[0].args]
  return dict(zip(arg_names, args))

def dformat(string, *args):
  return string.format(d(*args, d_name="dformat"))

def example(name, age, location, jank):

  # instead of writing this, over and over again
  print """Meet {name}, {age} years old, based out of {location}""".format(
      name=name, age=age, location=location)
  # coffeescript lets you write the dict part of that as
  # print """Meet {name}, {age} years old, based out of {location}""".format(
  #   {name, age, location})
  #
  # unfortunately, python already has {...} marked as set comprehension (2.7)
  #
  # you could use locals(), but they are rather insecure - it IS nice to
  # specify which values you want to pass
  #
  # so I propose instead the function d, prototyped above:
  print """Meet {name}, {age} years old, based out of {location}""".format(
      **d(
        name,
        age,
        location))

  # or, for the string formatting case, dformat
  #print dformat("""Meet {name}, {age} years old, based out of {location}""",
  #    name, age, location)

if __name__ == "__main__":
    example("@alexeymk", 26, "San Francisco", "this should remain private")
