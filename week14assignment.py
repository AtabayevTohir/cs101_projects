def map_products(manifest):
    product_map = {}
    for item in manifest:
        barcode = item["barcode"]
        name = item["product_name"]
        product_map[barcode] = name
    return product_map

def compare_shipment(product_map, scanned_barcodes):
    scanned_set = set(scanned_barcodes)
    map_set = set(product_map)
    missing_items = map_set - scanned_set
    extra_items = scanned_set - map_set
    return missing_items, extra_items

def calculate_missing_value(manifest, missing_set):
    return round(
        sum(item["price"] for item in manifest if item["barcode"] in missing_set),
        2
    )

manifest = [
    {"barcode": "A123", "product_name": "Laptop", "price": 1000.00},
    {"barcode": "B456", "product_name": "Mouse", "price": 25.50},
    {"barcode": "C789", "product_name": "Monitor", "price": 200.00}
]

scanned = ["A123", "B456", "D000"]

product_map = map_products(manifest)
missing, extra = compare_shipment(product_map, scanned)
lost_value = calculate_missing_value(manifest, missing)
print("Missing Barcodes:", missing)
print("Extra Barcodes:", extra)
print("Total Value Lost:", lost_value)
