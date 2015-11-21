python parsers/billboard.py hp > playlists/billboardhp.txt
python parsers/billboard.py alt > playlists/billboardalt.txt
python parsers/billboard.py top > playlists/billboardtop.txt
python parsers/billboard_realtime.py 24h > playlists/billboard24h.txt
python parsers/billboard_realtime.py tr140 > playlists/billboardtr140.txt
python parsers/billboard_realtime.py emrg > playlists/billboardemrg.txt

python ImportList.py playlists/billboardhp.txt e643cd9a-92d5-416e-8e16-1827cf006b53
python ImportList.py playlists/billboardalt.txt dfae72e6-0585-4122-9ac7-3f863cb6c72f
python ImportList.py playlists/billboardtop.txt dcb65ce1-e24c-4ea0-b87d-41e5460cd559
python ImportList.py playlists/billboard24h.txt b0b9372b-0d99-4157-8ecc-26d164096ad7