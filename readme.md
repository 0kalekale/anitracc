# Anitracc

anilist.co frontend in flask. why? the website is too bloated, i need something that just werks.

## install 

```
make install
```

## run the server

```
make setup  # only needed for the first time and after `make clean`
make run    # run the server
```

## clean up

```
make clean  # deletes everything from the previous instance
```

it works by saving your api token in instance/config.json, go to '/login' to authenticate

(note: this is only intended to run on localhost)

work in progress.
