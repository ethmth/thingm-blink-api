# ThingM Blink(1) API

A simple Rest API for the ThingM Blink1 Device that allows for network control using Python, Flask, and Docker.

In this project, I use the existing python library for the ThingM blink1 to create a flask API, so that I can control the blink1 device over the network.

This will only work if you have a ThingM device connected to your PC.
It is intended to be run in a docker container.

## Requirements

You will need a ThingM Blink1 light device plugged into the system you are running the API on.

The API requires `docker` and `docker-compose`.

## Setup

### Getting the Files

Ensure `git` is installed, then clone the git repo.

```sh
git clone https://github.com/ethmth/thingm-blink-api.git
cd thingm-blink-api/
```

### Configuration

The API is set to run on port `5000` in a docker container named `blink-api`. If you would like to change either of these values, edit the `.env` file.

## Running the API

While in the repo directory, run the API using docker compose.

```sh
docker-compose up
```

Alternatively, you can set the API to run in the background.

```sh
docker-compose up -d
```

Stop the background container by entering the repo directory and running `docker-compose stop`

Allow docker some time to create the image and start the container before testing.

## Usage

### /fade

To turn the blink device on, use the `/fade` endpoint with the `color` and `time` query components. `color` can be a simple, plain-text color, a hexadecimal value, or RGB values separated by commas. `time` is the milliseconds it takes to change to that color completely from its existing state.

Example usages:

```sh
curl 'localhost:5000/fade?color=red&time=1500'
curl 'localhost:5000/fade?color=212,78,65'
curl 'localhost:5000/fade?color=#da4354&time=10'
```

### /blink

The `/blink` endpoint also takes `color` and `time` query components. `color` follows the same rules as before, but now `time` is the milliseconds it takes to continuously alternate between the color specified and no light. This achieves a blinking effect.

Example usages:

```sh
curl 'localhost:5000/blink?color=blue'
curl 'localhost:5000/blink?color=#abab64&time=101'
curl 'localhost:5000/blink?color=45,232,12&time=2500'
```

### /off

The `/off` endpoint takes no query parameters and simply sets the blink device to emit no light.

Example usage:

```sh
curl 'localhost:5000/off'
```
