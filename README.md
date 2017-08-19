# FaaS Swarm Checkin

Using the great [Open FaaS](https://github.com/alexellis/faas), you can easily check-in on Swarm/Foursquare by making a request to this function. Be sure to supply 
your own OAuth token and venue ID in the `stack.yml`.

## Deploying the function

Follow the instructions on the [FaaS repo](https://github.com/alexellis/faas) to deploy the Faas stack.

**Get the CLI**

You can install the [faas-cli](https://github.com/alexellis/faas-cli/) via `brew install faas-cli` or `curl -sSL https://get.openfaas.com | sudo sh`.

**Build and deploy**

Build and deploy your stack using the following commands:

```
$ faas-cli -action build -f ./stack.yml
$ faas-cli -action deploy -f ./stack.yml
```

**Test**

Using `curl`, you can send an empty payload to the function to check-in:

```
$ curl localhost:8080/function/swarm_checkin -d ''
```

That's it. You're checked in!

You can hook this up with [IFTTT](https://ifttt.com) to automatically check you in to places when you arrive there. Give it a shot!
