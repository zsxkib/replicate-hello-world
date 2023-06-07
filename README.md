# **Replicate Hello World with Cog** 🌍

Welcome to the `replicate-hello-world` project! This is a simple "Hello World" function designed to help me get started with [Cog](https://github.com/replicate/cog) and [Replicate](https://replicate.com/).

If you're also new to [Cog](https://github.com/replicate/cog) and [Replicate](https://replicate.com/) you should check out the [code](https://github.com/zsxkib/replicate-hello-world)!

## Project Overview 🔮

This project contains a Python script that defines a greeting predictor. The predictor is a simple function that takes a name as input and returns a greeting message.

If you'd like details on how to push your own HelloWorld model, read on! ⚙️<br>
Otherwise, just type in a `"name"` into the [Replicate instance!](https://replicate.com/zsxkib/hello-world) 🖍️
___

### Predictor Class Overview 🚀

The `Predictor` class in our script extends the `BasePredictor` class from the Cog library. It consists of two main methods:

1. `setup()`: This method is called once during the initialization of the `Predictor` instance. It's used to set up any necessary attributes or data for the `Predictor`. In our case, we're initializing a `greetings` attribute with the string "Hello".

2. `predict(name: str)`: This method is the core of our model. It's called to make predictions based on the provided `name`. It uses the `greetings` attribute of the instance and the provided `name` to create a greeting message. The `name` is passed as an argument to the `predict` method.

Here's a simple example of how to use the `Predictor`:

```python
> p = Predictor()
> print(p.predict("Sakib"))

Hello, Sakib!
```

## Running the Model Locally 🏡

To run the model locally, you will first need to build it using Cog. You can do this by running the following command in your terminal:

```zsh
$ cog build
```

This command will build a Docker image of the model.

After building the model, you can make a prediction by running the following command:

```zsh
$ cog predict -i name="Sakib"
```

This command will start a Docker container of the model and make a prediction using the input you provided (`"Sakib"` in this case). You should see output similar to the following:

```
Running prediction...
Hello, Sakib!
```

This indicates that the model successfully made a prediction.

Note that the specifics of how to use the `cog` command may depend on your setup and environment, so be sure to consult the [Cog documentation](https://github.com/replicate/cog) for more detailed information.
