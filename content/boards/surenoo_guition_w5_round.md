Title: MicroPython for Surenoo Guition W5 Round
Date: 2025-07-05 10:30
Category: Board
Tags: esp32, esp32-s3, surenoo

Follow the steps below to install MicroPython on your Surenoo Guition W5 Round
ESP32S3 board from your browser. You can review or rebuild the source code using
the [project repo](https://github.com/mp-extras/SURENOO_GUITION_W5_ROUND).

* Connect board to PC using USB-C cable
* Press the Connect button below and follow prompts (use serial port USB JTAG/serial debug unit)

<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>
<esp-web-install-button manifest="binaries/surenoo_guition_w5_round/manifest.json">
    <span slot="unsupported">Your browser does not support WebSerial</span>
    <span slot="not-allowed">You are not allowed to use this on HTTP</span>
</esp-web-install-button>

Web installation is thanks to the [ESP Web Tools](https://esphome.github.io/esp-web-tools) project.
