Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to read API documentation to find the endpoints you’re looking for
How to use an API with pagination
How to parse JSON results from an API
How to make a recursive API call
How to sort a dictionary by value

How to read API documentation to find the endpoints you’re looking for:

API documentation typically provides information about the endpoints available, along with their descriptions, parameters, and expected responses. Look for sections like "Endpoints", "Resources", or "Routes" in the documentation to find the list of available endpoints. Pay attention to the HTTP methods (GET, POST, PUT, DELETE) associated with each endpoint and their purpose.
How to use an API with pagination:

Pagination is a technique used by APIs to limit the number of results returned in a single response. This is often necessary when dealing with large datasets to improve performance. Pagination is usually implemented using query parameters like page and per_page or limit to specify the page number and number of results per page, respectively. The API response typically includes metadata like total_count, next, and previous links to navigate through the paginated results.
How to parse JSON results from an API:

JSON (JavaScript Object Notation) is a lightweight data interchange format commonly used by APIs to transmit data. Parsing JSON involves converting the JSON-formatted data received from the API into a usable data structure in your programming language (e.g., dictionaries, lists). Most programming languages provide built-in libraries or modules for parsing JSON. Once parsed, you can access the data elements using the appropriate syntax for your chosen programming language.
How to make a recursive API call:

Recursive API calls involve making repeated API requests within a function until a certain condition is met. This is often used when dealing with hierarchical data structures or when paginating through large datasets. To implement recursive API calls, define a function that makes the API request and processes the response. Within the function, check if there are more pages or additional data to fetch, and if so, make another API call recursively until the desired data is retrieved.
How to sort a dictionary by value:

Sorting a dictionary by value involves rearranging its key-value pairs based on the values rather than the keys. In most programming languages, dictionaries are inherently unordered collections, so you'll need to use additional functions or methods to achieve sorting. Depending on the programming language, you can use built-in functions or libraries to sort dictionaries by their values. Typically, you'll extract the key-value pairs into a list of tuples, sort the list based on the values, and then reconstruct the dictionary from the sorted list of tuples.





