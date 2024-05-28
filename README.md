<br>
<p align="center">
  <img src="https://github.com/germainechu/remy-open-source/assets/45610419/54a709b0-2923-4c9d-96d1-cd4e6541d614" width="100" height="100">
</p>

# Introduction
Welcome to REMY’s open source community! We are a core team of developers, product designers, and big picture thinkers that want to help shape the future of how AI can improve our human ability to become a better human. 

REMY stands for “RE-imagine MY-self”. It’s our belief that everyone is a better version of themselves when they connect with the best people around them. The only thing holding people back from making these connections is the logistical friction that constrains our lives and the ability to connect. By actioning information about the spaces and people that inhabit them through deeper, more insightful analysis - we can empower people are to reach out and be present with one another in a more meaningful way. 

Our open source vision is to create a community where developers passionate about the problem space can collaborate and solve pieces of the puzzle together. We are currently a start-up looking to hire part-time and full-time engineers, and we see this open source community as the place to begin growing our connections to talent organically. What this means for you, is if you’re interested in us, and we’re interested in you, we would be excited to open a discussion to full-time employment with REMY and see how we can best support one another in building a better world, together. 

# Key Information
<img src="https://github.com/germainechu/remy-open-source/assets/45610419/54a4fafc-b91e-474a-bacf-7079c6894bea" width="20" height="20">
Github: https://github.com/germainechu/remy-open-source
<br>
<img src="https://github.com/germainechu/remy-open-source/assets/45610419/d019c464-bc7d-4073-a91d-4d102f47336e" width="25" height="25">
Discord: https://discord.gg/9uw6w6tqBg 

# Main Contacts: 
Germaine - Co-founder of REMY. She graduated from the University of British Columbia with a Bachelors in Mathematics. She is currently working as a senior software engineer at Workday, and is a huge nerd about building cool technology, alongside great people with brilliant minds.

<img src="https://github.com/germainechu/remy-open-source/assets/45610419/7c1b71dd-630d-4197-bd03-7ae182917675" width="25" height="25">
Linkedin: https://www.linkedin.com/in/germaine-chu-08a02b187/ 
<br>
<img src="https://github.com/germainechu/remy-open-source/assets/45610419/d019c464-bc7d-4073-a91d-4d102f47336e" width="25" height="25">
Discord: @grrchu 

# Engineering Best Practices
We expect clean and readable code as the basis for our repo. When another developer takes a look at your code, they should be able to skim over it and understand not only how you chose to implement your solution, but most importantly - why you chose to implement it in this way. 

Given most of our open source challenges will be around data science, ML, and optimizing cutting edge AI research into our experiments, the primary language used will be Python. However, if you find your solution requires more than Python, please use the guidelines below as best practices across all languages. If you have questions about coding standards, or naming conventions, please reach out to us on Discord to discuss further. 

### General Python Conventions:
* **Indentation**: Use 4 spaces per indentation level.
* **Blank Lines**: Use blank lines to separate functions and classes, and larger blocks of code inside functions.

### Naming Conventions
* **Variables**: Use lowercase words separated by underscores (e.g., variable_name).
* **Functions**: Use lowercase words separated by underscores (e.g., function_name()).
* **Classes**: Use CapitalizedWords (CamelCase) convention (e.g., ClassName).
* **Constants**: Use uppercase words separated by underscores (e.g., CONSTANT_NAME).

### Documentation
* **Docstrings**: Use triple quotes for docstrings to describe modules, classes, and functions. 
* **Comments**: Use comments to explain why code does something, not what it does. Ensure comments are up-to-date, relevant, and explain the purpose clearly. 

```
# This is a code snippet for demonstrating Python Best Practices

# A constant representing the maximum allowed value
MAX_VALUE = 100

class ExampleClass:
    """
    This class demonstrates the naming conventions for classes and methods.
    """

    def update_value(self, new_value):
        """
        Update the current value with a new value, if it's within the allowed range.

        Args:
            new_value (int): The new value to update.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if new_value <= MAX_ALLOWED_VALUE:
            self.current_value = new_value
            return True
        else:
            return False
```
### Imports
Import standard libraries first, followed by third-party libraries, and then local imports. Separate each group with a blank line.
<br>
Please avoid wildcard imports where you can (e.g., from module import *).

### Error Handling
Use exceptions appropriately. Catch specific exceptions rather than using a blanket except clause. This allows all contributors to debug and have context on why something is failing, which means we can solve problems faster, together. 
<br>
Use try-except blocks to handle errors gracefully and provide meaningful error messages.

### Code Structure
* **Modularity**: Always aim to break down your code into reusable functions and classes. If you notice an opportunity to refactor, take the time to! Refactoring allows us to reduce errors, have better debugging, and most importantly - maintain readability. 
* **Single Responsibility**: Like you’ve learned in school, each function or class should have a single responsibility or purpose. Once again, this helps maintain readability and scalability. We can prevent erroneous mistakes when we can simplify what each piece of our code contributes to the solution.

### Testing
* **Unit Tests**: Please write unit tests for your functions. We encourage you to install and use pytest as it allows you to write tests in a very simple and straightforward manner using plain functions, instead of classes like you would in unittest. 
* **System / Integration Tests**: Where appropriate, system tests may also be necessary. Please avoid mocking data in integration / system tests, as using instances of external dependencies such as databases or APIs will allow us to avoid false positives, and ensure better production level code. 
* **Edge Cases**: This goes without saying, but be diligent with edge cases. Reach out in the discord if you’re having trouble coming up with edge cases to test, as this is a productive brainstorming opportunity for contributors to collaborate and understand what the community is working on!

### Version Control
* **Commits**: Commit code frequently with meaningful commit messages. We encourage smaller commits that can later be squashed when merging. Similar to the single responsibility principle, each commit should represent a chunk of logic that contributes to the solution. 

### Branching Strategy: 
We will have two core branches - **Master** and **Development**. 
* *Master* - the main branch that will store official release history. Only code that has been fully tested, approved for production, and is functionally passing all tests should be merged into master. Master will be locked until approval is granted. 
* *Development* - the development branch is the main integration branch for features. All feature development should be merged into this branch before merging into master. 
<br>

We will have two supporting branches - **Feature** and **Release**.

* *Feature* - each new feature should be developed in its own branch, branched off from the development branch. When naming your feature branch, please put “feature/<issue-number>-<description>”. 
  * For example, “feature/45-search-filters”
* *Release* - when development has acquired enough features for a release, a release branch is created from development. This branch allows for final testing, bug fixes, and preparing metadata for a release. Once ready, this branch will be merged into development, which will then be merged back into master. 

### Code Reviews
Please participate in code reviews to maintain code quality and to see what other devs are up to! This is a great opportunity to ask questions, be curious, and learn about their solution and strategy.
<br>
Aim to be as constructive as possible, questions are always welcome, as well as sharing resources or alternative implementation strategies backed by tutorials or documentation is also welcome. 

# Project Management
Woo! Engineering standards are always a dry thing to go through, but we’re almost done. 

You can find all tasks and issues in the *github repo* through the *project board*. We’ll be updating it with new issues regularly. 
<br>
Key milestones and deadlines will also be updated in the project board, deadlines are mostly self-defined, but required you as the developer to know your own schedule, bandwidth and most importantly - know how your code is interacting with other contributors. 
<br> 
If your feature is blocking another dev’s, please be mindful of their time, and be as efficient as possible at unblocking one another. 
	
# Submitting Work
Finally, submitting your work. 

### Pull Requests:
* Keep your PRs *small and focused*. They should focus on a single concern or feature. Large PRs are naturally harder to review and risk introducing bugs. Good rule of thumb, try to keep your PRs under 200-400 lines of code changes. 
* Write the *titles of your PRs concisely, and with clear descriptions*. The title should concisely summarize the changes, while the description aims to provide more context, explain the why behind the changes, along with calling out any relevant tasks or issues. 
* Follow *consistent naming conventions*, your PR should be the same as the branch names. If your branch is “feature/42-data-setup”, then your PR should be named the accordingly. 
Create draft PRs for early feedback, which allows us to pre-test and for you to get early feedback from other contributors before finalizing the changes. This allows us to catch issues earlier on, rather than later in production. 

And that’s it! Welcome to our open-source community - we are so happy to have you here. 
