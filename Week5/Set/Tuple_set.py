#We can also initialise a set with other immutable data structures such as a tuple. Tuples do
def observed(): #function named observed has no parameters.
  web_browser_usage = {("Chrome", 10), ("Firefox", 9), ("Edge", 3)} 
  web_browser_usage.add(("Opera", 1))
  web_browser_usage.remove(("Edge", 3))
  web_browser_usage.add(("Opera", 1)) # doesn't add another Opera as its a tuple

  return web_browser_usage

def run():
  print(observed())

run ()