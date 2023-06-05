from cog import BasePredictor, Input


class Predictor(BasePredictor):
    def setup(self):
        """Set up the Predictor instance by initializing its attributes.

        This method is called once during the initialization of the Predictor instance.
        It sets the value of the 'greetings' attribute to "Hello".
        """

        self.greetings = "Hello"

    def predict(self, name: str = Input(description="Your name")) -> str:
        """Predict a greeting message with the provided name.

        This method is called to make predictions based on the provided name.
        It uses the 'greetings' attribute of the instance and the provided name to create a greeting message.

        Parameters
        ----------
        name : str
            The name that will be included in the greeting message.

        Returns
        -------
        str
            The greeting message with the provided name.

        Examples
        --------
        >>> p = Predictor()
        >>> p.predict("Alice")
        'Hello, Alice!'
        """

        return f"{self.greetings}, {name}!"
