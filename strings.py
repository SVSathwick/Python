# print("Hello")
# print('Hello')

# name='Sathwick'
# print(name)

# #Multiline Strings-Triple quotes will let us do it
# googleNews = """Google News is a news aggregator service developed by Google. 
#               It presents a continuous flow of links to articles organized from thousands of publishers and magazines. 
#               Google News is available as an app on Android, iOS, and the Web."""
# print(googleNews)

#Three single quotes also works
# sampleText = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(sampleText)

# words = "hello"
# print(words[0])
# print(words[1])
# for x in words:
#     print(x)
# for c in "world":
#     print(c)

fullname = 'Venkata Sathwick Sivvala'
print('length of ' + str(fullname) + ' is ' + str(len(fullname)))

txt = 'the best things in life is free'
print('free' in txt)
if 'best' in txt:
    print('best is present in ' + txt)
if 'hello' not in txt:
    print('hello is not present in ' + txt)