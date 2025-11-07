def receive_new_shipments(shipments, new_shipments):
    for i in new_shipments:
        shipments.append(i)


def dispatch_shipments(shipments, num_to_dispatch):
    if num_to_dispatch > len(shipments):
        num_to_dispatch = len(shipments)
    dispatched = shipments[:num_to_dispatch]
    shipments[:] = shipments[num_to_dispatch:]
    return dispatched

def recall_shipment(shipments, shipment_id):
    for i in shipments:
        if i == shipment_id:
            shipments.remove(i)
            return True
    return False

def manage_shipments(initial_shipments, new_shipments_to_receive, shipments_to_dispatch, shipment_to_recall):
    final_shipments_list = []
    for item in initial_shipments:
        final_shipments_list.append(item)
    receive_new_shipments(final_shipments_list,new_shipments_to_receive)
    recall_shipment(final_shipments_list,shipment_to_recall)
    dispatched_shipments_list = dispatch_shipments(final_shipments_list,shipments_to_dispatch)
    return final_shipments_list, dispatched_shipments_list

initial = ["BOX-A1", "BOX-B2", "BOX-C3", "BOX-D4"]
new = ["BOX-E5", "BOX-F6"]
dispatch_count = 2
recall_id = "BOX-D4"

# When you call your function, you can receive the two returned lists like this:
final_state, dispatched = manage_shipments(initial, new, dispatch_count, recall_id)
print('Test Case 1 Results:')
print(f'final_state: {final_state}')
print(f'dispatched: {dispatched}')
print(f'\nOriginal list unchanged: {initial}')












# a = ["BOX-A1", "BOX-B2", "BOX-C3", "BOX-D4"]
# b = 35
# print(dispatch_shipments(a,b))