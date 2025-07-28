"""Core functionality for my_package."""


def greet(name: str = "World") -> str:
    """Generate a greeting message.
    
    Args:
        name: The name to greet. Defaults to "World".
        
    Returns:
        A greeting string.
        
    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
        
    Examples:
        >>> add_numbers(2, 3)
        5.0
        >>> add_numbers(2.5, 3.7)
        6.2
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
        
    Examples:
        >>> multiply(3, 4)
        12.0
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


class Calculator:
    """A simple calculator class.
    
    Examples:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5.0
        >>> calc.result
        5.0
    """
    
    def __init__(self):
        """Initialize calculator with result of 0."""
        self.result = 0.0
    
    def add(self, value: float) -> float:
        """Add a value to the current result.
        
        Args:
            value: Value to add
            
        Returns:
            The new result
        """
        self.result += value
        return self.result
    
    def subtract(self, value: float) -> float:
        """Subtract a value from the current result.
        
        Args:
            value: Value to subtract
            
        Returns:
            The new result
        """
        self.result -= value
        return self.result
    
    def multiply_by(self, value: float) -> float:
        """Multiply the current result by a value.
        
        Args:
            value: Value to multiply by
            
        Returns:
            The new result
        """
        self.result *= value
        return self.result
    
    def clear(self) -> None:
        """Reset the calculator to 0."""
        self.result = 0.0
