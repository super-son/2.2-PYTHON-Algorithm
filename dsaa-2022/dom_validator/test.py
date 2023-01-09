import my_dom_validator as ds
dom_text = """<items>
             <data>
                 <items name="item1">item1abc</items>
                 <item name="item2">item2abc</item>
             </items>
         </data>
         """.strip()

print(ds.is_validate_dom(dom_text))
# for i in dom_text.split('<'):
#     print(i)