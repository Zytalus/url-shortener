
# URL Shortener

This example project uses AWS CDK create a URL shortener with python. The application
creates AWS resources to support its functionality. AWS API Gateway provides a
front-end endpoint for end users. AWS Lambda provides the functionality of
creating and reading short urls. AWS DynamoDB Table for storing and retrieving
the original urls and short 8-digit UUID codes. AWS Route53 creates a record
to point a custom domain to the API Gateway. AWS Certificate Manager provides
the API Gateway with a certificate to support HTTPS traffic over port 443.

![URL Shortener Architecture Diagram](url-shortener.png)

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization 
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on macOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

Update the config.py file to reflect your resources

```
$ nano config.py
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
