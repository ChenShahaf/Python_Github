print("Practice 18 of 18 - Lambda Expressions")
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = (list(filter(lambda x: x != "X", garbled,)))
spaces_words = "".join(message)
spaces_words.split()
print(spaces_words)