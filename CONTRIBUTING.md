# Contributing to nepali-num2word

Thank you for your interest in contributing to `nepali-num2word`! This document provides guidelines and information for contributors.

## 🎯 Ways to Contribute

- 🐛 **Bug Reports**: Report issues or unexpected behavior
- 💡 **Feature Requests**: Suggest new features or improvements
- 📝 **Documentation**: Improve documentation, examples, or tutorials
- 🔧 **Code Contributions**: Fix bugs, implement features, or optimize performance
- 🌍 **Localization**: Help with Nepali language accuracy and cultural nuances
- 🧪 **Testing**: Write tests, improve test coverage, or test edge cases

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of Nepali numbering system
- Familiarity with Python development practices

### Development Setup

1. **Fork and Clone**
   ```bash
   # Fork the repository on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/nepali-num2word.git
   cd nepali-num2word
   ```

2. **Create Virtual Environment**
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   # Install in development mode
   pip install -e .
   
   # Install development dependencies
   pip install pytest pytest-cov black flake8 mypy
   ```

4. **Verify Installation**
   ```bash
   # Test the CLI
   python cli/main.py 123456 --lang np
   
   # Run tests
   python -m pytest tests/
   ```

## 📋 Development Workflow

### 1. Create a Feature Branch

```bash
# Always create a new branch for your work
git checkout -b feature/your-feature-name

# Examples:
git checkout -b feature/add-ordinal-numbers
git checkout -b fix/decimal-precision-issue
git checkout -b docs/improve-examples
```

### 2. Make Your Changes

- Follow the existing code style and patterns
- Write clear, self-documenting code
- Add docstrings for new functions and classes
- Update relevant documentation

### 3. Write Tests

```bash
# Create test files in the tests/ directory
# Test file naming: test_<module_name>.py

# Example test structure:
def test_convert_basic_numbers():
    assert convert_to_words(123) == "one hundred twenty-three"

def test_convert_nepali_unicode():
    assert convert_to_words(123, lang='np') == "एक सय तेइस"
```

### 4. Run Quality Checks

```bash
# Run tests
python -m pytest tests/ -v

# Check code coverage
python -m pytest tests/ --cov=nepali_num2word --cov-report=html

# Format code
black nepali_num2word/ tests/ cli/

# Check linting
flake8 nepali_num2word/ tests/ cli/

# Type checking
mypy nepali_num2word/
```

### 5. Commit Your Changes

```bash
# Add your changes
git add .

# Write a clear commit message
git commit -m "feat: add support for ordinal numbers

- Implement ordinal number conversion (1st, 2nd, 3rd, etc.)
- Add tests for ordinal number functionality
- Update documentation with ordinal examples"
```

#### Commit Message Guidelines

Use conventional commit format:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Build process or auxiliary tool changes

### 6. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create a pull request on GitHub
```

## 🔍 Code Style Guidelines

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use `black` for code formatting
- Maximum line length: 88 characters
- Use meaningful variable and function names
- Add type hints where appropriate

```python
# Good example
def convert_to_words(number: Union[int, float, str], lang: str = 'en') -> str:
    """Convert number to words in Nepali numbering system.
    
    Args:
        number: Number to convert (int, float, or numeric string)
        lang: Language code ('en' for English, 'np' for Nepali)
        
    Returns:
        Number converted to words
        
    Raises:
        TypeError: If input type is invalid
        ValueError: If number is out of supported range
    """
    # Implementation here
    pass
```

### Documentation Style

- Use clear, concise language
- Provide examples for complex functionality
- Document all parameters, return values, and exceptions
- Include usage examples in docstrings

### Error Handling

- Provide clear, actionable error messages
- Use appropriate exception types
- Include context in error messages

```python
# Good error handling
if not isinstance(number, (int, float, str)):
    raise TypeError(
        f"Unsupported type: {type(number).__name__}. "
        f"Expected int, float, or numeric string"
    )
```

## 🧪 Testing Guidelines

### Test Structure

- Create comprehensive test cases for all functionality
- Test both positive and negative cases
- Include edge cases and boundary conditions
- Test error conditions and exception handling

### Test Categories

1. **Unit Tests**: Test individual functions
2. **Integration Tests**: Test CLI commands
3. **Edge Case Tests**: Test boundary conditions
4. **Error Tests**: Test error handling

### Example Test

```python
import pytest
from nepali_num2word import convert_to_words

class TestConvertToWords:
    
    def test_basic_conversion(self):
        """Test basic number conversion."""
        assert convert_to_words(123) == "one hundred twenty-three"
        assert convert_to_words(1000) == "one thousand"
    
    def test_nepali_unicode(self):
        """Test Nepali Unicode output."""
        assert convert_to_words(123, lang='np') == "एक सय तेइस"
    
    def test_error_handling(self):
        """Test error conditions."""
        with pytest.raises(TypeError):
            convert_to_words(None)
        
        with pytest.raises(ValueError):
            convert_to_words("invalid")
```

## 🌍 Nepali Language Guidelines

### Cultural Accuracy

- Ensure Nepali translations are culturally appropriate
- Use standard Nepali numbering conventions
- Verify Unicode characters are correct

### Language Review Process

- Nepali language changes require review by native speakers
- Include context for cultural or linguistic decisions
- Test with various Nepali fonts and systems

## 📖 Documentation Guidelines

### README Updates

- Update examples when adding new features
- Ensure all features are documented
- Keep installation instructions current

### API Documentation

- Document all public functions and classes
- Include parameter types and descriptions
- Provide usage examples
- Document exceptions and error conditions

### Changelog

- Add entries to CHANGELOG.md for all user-facing changes
- Follow [Keep a Changelog](https://keepachangelog.com/) format
- Include migration notes for breaking changes

## 🚀 Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Version number is bumped
- [ ] CHANGELOG.md is updated
- [ ] GitHub release is created
- [ ] PyPI package is published

## 🎯 Feature Request Guidelines

### Before Submitting

1. Check existing issues and discussions
2. Ensure the feature aligns with project goals
3. Consider implementation complexity
4. Think about backward compatibility

### Feature Request Template

```markdown
**Feature Description**
Brief description of the proposed feature.

**Use Case**
Explain why this feature would be useful.

**Proposed Implementation**
If you have ideas about how to implement this.

**Additional Context**
Any other relevant information.
```

## 🐛 Bug Report Guidelines

### Bug Report Template

```markdown
**Bug Description**
Clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Call function with parameters...
2. Expected result...
3. Actual result...

**Expected Behavior**
What you expected to happen.

**Environment**
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Python version: [e.g., 3.9.7]
- Package version: [e.g., 1.0.0]

**Additional Context**
Any other context about the problem.
```

## 🤝 Code Review Process

### For Contributors

- Respond to review feedback promptly
- Ask questions if feedback is unclear
- Make requested changes in separate commits
- Squash commits before merge if requested

### For Reviewers

- Be constructive and respectful
- Focus on code quality and maintainability
- Test the changes locally when possible
- Provide clear, actionable feedback

## 💬 Communication

### Channels

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: General questions, ideas
- **Pull Requests**: Code review discussions

### Guidelines

- Be respectful and inclusive
- Use English for all communication
- Provide context for your questions
- Search existing discussions before posting

## 📜 License

By contributing to `nepali-num2word`, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- GitHub contributors list
- README.md acknowledgments
- Release notes (for significant contributions)

## ❓ Questions?

If you have questions about contributing:

1. Check this guide first
2. Search existing GitHub issues and discussions
3. Create a new discussion for general questions
4. Create an issue for specific bugs or feature requests

Thank you for contributing to `nepali-num2word`! 🇳🇵