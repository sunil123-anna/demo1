Dictionary = {"string" : "https://www.google.com/search?q=string+meaning&rlz=1C1CHBF_enIN901IN901&oq=string&aqs=chrome.2.69i57j0l5j69i61l2.5768j0j7&sourceid=chrome&ie=UTF-8",
"Integer" : "https://www.google.com/search?rlz=1C1CHBF_enIN901IN901&sxsrf=ALeKk03ZRoues-07f-EZoP0W9StK9AosaA%3A1600756122081&ei=mplpX8fOBLWKmgex8oagDA&q=Integer+meaning&oq=Integer+meaning&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQkQIQRhD5ATICCAAyAggAMgIIADIGCAAQBxAeMgYIABAHEB4yAggAMgYIABAHEB4yCAgAEAcQChAeMgYIABAHEB46BwgAELEDEEM6BAgAEENQiYkEWIyXBGC5pQRoAHAAeACAAegBiAHlCZIBBTAuNC4zmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwjHg52gkfzrAhU1heYKHTG5AcQQ4dUDCA0&uact=5",
"Datatypes" : "https://www.google.com/search?rlz=1C1CHBF_enIN901IN901&sxsrf=ALeKk03-61riWk50HpMcbL90B4guImE_ig%3A1600756194015&ei=4plpX6hBx97Puw_csIWwBQ&q=data+type+meaning&oq=Dataty+meaning&gs_lcp=CgZwc3ktYWIQARgAMggIABAHEAoQHjIICAAQBxAKEB4yCAgAEAcQChAeMgYIABAHEB4yCAgAEAcQChAeMggIABAHEAoQHjIICAAQBxAKEB4yCAgAEAcQChAeMggIABAHEAoQHjIICAAQBxAKEB46CAgAELEDEJECOgIIADoECAAQClD1qQJY1ccCYOrlAmgAcAB4AIAB3QGIAbwHkgEFMC41LjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab",
}
#print(Dictionary)
val = input("Enter a word to be searched:")


print(Dictionary.get(val))