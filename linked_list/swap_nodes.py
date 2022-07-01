def swap_nodes(val_1, val_2, input_list):
    node_1 = input_list.get_head_node()
    node_2 = input_list.get_head_node()

    node_1_prev = None
    node_2_prev = None

    while node_1.next_node:
        if node_1.get_value() == val_1:
            break
        node_1_prev = node_1
        node_1 = node_1.get_next_node()

    while node_2.next_node:
        if node_2.get_value() == val_2:
            break
        node_2_prev = node_2
        node_2 = node_2.get_next_node()

    if node_1_prev == None:
        input_list.head_node = node_2
    else:
        node_1_prev.set_next_node(node_2)

    if node_2_prev == None:
        input_list.head_node = node_1
    else:
        node_2_prev.set_next_node(node_1)

    temp = node_1.get_next_node()
    node_1.set_next_node(node_2.get_next_node())
    node_2.set_next_node(temp)