# nowplaying.py

 Watches a text file with now playing data from radio automation software using inotify, then sends it (and/or generic branding slogans) to an Icecast stream and/or an RDS encoder.

## Dependencies

- inotify_simple
- requests
- websockets (for experimental Azuracast support)
- Exscript (for telnet support, only needed for RDS encoders)

## Compatibility

### Automation

| Software       | Supported | Details                    |
|----------------|-----------|----------------------------|
| Rivendell      | ✅        | Extensively tested with 3.x. Should work on 2.x and 4.x as well. |
| SAM Broadcaster | ✅        | Daily use with version 4.8. |
| Azuracast      | ❓        | EXPERIMENTAL and untested.   |

### RDS encoders

#### Inovonics

| Model          | Supported | Details                    |
|----------------|-----------|----------------------------|
| Novia 272      | ✅        |                            |
| Model 732      | ✅        |                            |
| Aaron 655      | ✅        |                            |
|                |           |                            |
| Model 730      | ❓        | Untested.                  |
| Model 720      | ❓        | May work with a telnet-serial bridge. Untested. |
| Model 713      | ❓        | Untested.                  |
| Model 712      | ❓        | May work with a telnet-serial bridge. Untested. |
| Model 711      | ❓        | May work with a telnet-serial bridge. Untested. |
|                |           |                            |
| Aaron 650      | ⛔        | No support for dynamic RDS, except when rebroadcasting RDS received from parent station. |
| INOmini 703    | ⛔        | No support for dynamic RDS.                     |
| INOmini 402    | ⛔        | Only rebroadcasts RDS recieved from parent station. |
| Model 710      | ⛔        | Only supports parallel port access from a DOS computer. I suppose support *could* someday be added, but ... who would need it? |
| Model 702      | ⛔        | No support for dynamic RDS.                     |
| Model 701      | ⛔        | No support for dynamic RDS.                     |

#### DEVA
**NOTE: Support for DEVA encoders is EXPERIMENTAL.** DEVA's online demos do not forward the necessary port to allow for testing. I have attempted a "best guess" implementation based on the product manuals, but your mileage *will* vary. (And will probably be zero, truthfully.)

| Model          | Supported | Details                    |
|----------------|-----------|----------------------------|
| SmartGen 6.0   | ❓        | Untested.                  |
| SmartGen 5.0   | ❓        | Untested.                  |
| SmartGen 4.1   | ❓        | Untested.                  |
| SmartGen Mini  | ❓        | Untested.                  |
|                |           |                            |
| SmartGen 3.1   | ⛔        | No support for "on-the-fly" dynamic RDS. |
| SmartGen Micro | ⛔        | No support for "on-the-fly" dynamic RDS. |

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)