def memory_addressing(page_table,page_size,logical_addressing):
    page_number,offset=divmod(logical_addressing,page_size)
    if page_number in page_table:
        frame_number=page_table[page_number]
        physical_address=frame_number*page_number+offset
        print(f"the physical address is{physical_address}")
    else:
        print("invalid page number,address translation faild")

page_table = {0: 5, 1: 9, 2: 14}
page_size=4096
logical_addressing=int(input("輸入地址"))

memory_addressing(page_table,page_size,logical_addressing)
