import bencodepy


def get_magnet_link(torrent_file_path):
    with open(torrent_file_path, 'rb') as file:
        torrent_data = bencodepy.decode(file.read())
        info_hash = torrent_data[b'info'][b'hash']
        magnet_link = f'magnet:?xt=urn:btih:{info_hash.decode()}'
        return magnet_link


print(get_magnet_link("C:\\Users\\ojasw\\Desktop\\magnetube\\torrent_to_magnet"))
