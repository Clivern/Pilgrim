<p align="center">
    <img alt="Midway Logo" src="/assets/img/logo.png" width="200" />
    <h3 align="center">Midway</h3>
    <p align="center">A Fast, Secure and Reliable Platform as a Service, Set up in Minutes.</p>
    <p align="center">
        <a href="https://github.com/Clivern/Midway/actions/workflows/api.yml">
            <img src="https://github.com/Clivern/Midway/actions/workflows/api.yml/badge.svg"/>
        </a>
        <a href="https://github.com/Clivern/Midway/releases">
            <img src="https://img.shields.io/badge/Version-0.1.0-1abc9c.svg">
        </a>
        <a href="https://github.com/Clivern/Midway/blob/master/LICENSE">
            <img src="https://img.shields.io/badge/LICENSE-Apache_2-e74c3c.svg">
        </a>
    </p>
</p>

`Midway` is a platform as a service (PaaS) built on a top of `django` that is designed to efficiently and securely provision and manage a fleet of Linux servers. It offers a reliable solution for deploying and configuring commonly used services, such as databases, message brokers, graphing, tracing, and caching tools, on a variety of cloud providers.


### Documentation

#### Getting Started

In order to run `midway`, you need `Python`, `Redis` and `MySQL`. Then run the following commands:

```zsh
# Create a python venv
$ python3 -m venv venv

$ make config
```

To run the application:

```zsh
$ make create-env

# To run the Web UI
$ make run

# To run workers
$ make worker
```

To run test cases:

```zsh
$ make ci
```

To list all commands:

```zsh
$ make
```


### Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, `Midway` is maintained under the [Semantic Versioning guidelines](https://semver.org/) and release process is predictable and business-friendly.

See the [Releases section of our GitHub project](https://github.com/clivern/midway/releases) for changelogs for each release version of `Midway`. It contains summaries of the most noteworthy changes made in each release. Also see the [Milestones section](https://github.com/clivern/midway/milestones) for the future roadmap.


### Bug tracker

If you have any suggestions, bug reports, or annoyances please report them to our issue tracker at https://github.com/clivern/midway/issues


### Security Issues

If you discover a security vulnerability within `Midway`, please send an email to [hello@clivern.com](mailto:hello@clivern.com)


### Contributing

We are an open source, community-driven project so please feel free to join us. see the [contributing guidelines](CONTRIBUTING.md) for more details.


### Credits

Shoutout to these open source projects and their maintainers.

- [Django.](https://www.djangoproject.com/)
- [Django-RQ](https://github.com/rq/django-rq)
- [Requests](https://github.com/psf/requests)
- [Ansible Runner](https://github.com/ansible/ansible-runner)
- [VueJs](https://github.com/vuejs/vue)
- [Tabler](https://github.com/tabler/tabler)
- [and other projects ...](requirements.txt)


### License

© 2022, `Midway`. Released under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**Midway** is authored and maintained by [@Clivern](https://github.com/clivern).
