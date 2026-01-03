def update_file(import_file, remove_list):
    """
    Updates an IP allowlist by removing specified IP addresses.
    """

    with open(import_file, "r") as file:
        ip_addresses = file.read().split()

    ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]

    with open(import_file, "w") as file:
        file.write(" ".join(ip_addresses))


if __name__ == "__main__":
    update_file(
        "allow_list.txt",
        ["192.168.25.60", "192.168.140.81", "192.168.203.198"]
    )
