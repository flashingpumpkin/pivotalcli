# pivotalcli

Ever found you want to add a lot of stories for lots of files to
Pivotal Tracker but found it too much hassle to do by hand? Enter
`pivotalcli`:

    find templates/ -name "*html" | xargs -I {} pivotalcli add {} --labels "templates, todo"
    
That is it, in a nutshell. 

## Installation

    pip install pivotalcli

## Configuration

`pivotalcli` looks first for `--token` and `--project` flags. If that
fails it looks for `PIVOTAL_[TOKEN|PROJECT]` env vars. If
that also fails, it walks up your file tree until it finds a `.pivotal.json`
file with `TOKEN` and `PROJECT` keys, eg:

    {"PROJECT": "123", "TOKEN": "456"}

