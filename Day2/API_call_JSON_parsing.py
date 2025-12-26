import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

# print(response.text)
a = response.json()

print("\n JSON type of a:", type(a), "\n")   # This will print <class 'list'>.  Now so you know that it is a list type. How to iterate a list?


print("what does the list holds inside?\n", a[0].keys())  
# This will print the first item in the list)
print("\nAbove line shows Keys in the first post dictionary:\n")

print("\ntotal number of posts:\n", len(a), "\n")  # This will print total number of posts in the list

print("First 5 posts title and body:\n")

for item in a[:5]:   # Print only first 5 items to avoid too much output
     print(f"Title: {item['title']}\nBody: {item['body']}\n")

# Writing first 5 posts to a JSON file

with open("posts.json", "w") as f:
    json.dump(a[:5], f, indent=4)  # Dump first 5 posts into the file with indentation of 4 spaces
    print("First 5 posts have been written to posts.json")


# what is f?
# f is a file object that is used to write data to the file posts.json
# json.dump() method is used to write JSON data to a file
# indent parameter is used to format the JSON data with indentation for better readability

# what is indent=4?
# indent=4 means that each level of the JSON data will be indented by 4 spaces
# This makes the JSON data more readable when you open the file

# List is a collection of items that are ordered and changeable. 
# In this case, the list contains multiple dictionaries.
# each representing a post with keys like 'userId', 'id', 'title', and 'body'.