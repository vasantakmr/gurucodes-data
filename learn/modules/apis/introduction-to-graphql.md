---
title: "Introduction to GraphQL"
---

### What is GraphQL?

**GraphQL** is a query language for APIs that provides a more flexible and efficient way to request exactly the data you need from an API. Unlike REST, where you may receive more data than needed, GraphQL allows you to request only specific fields, minimizing over-fetching.

### Key Features of GraphQL

- **Single Endpoint**: Unlike REST, which uses different endpoints for different resources, GraphQL uses a single `/graphql` endpoint for all requests.
- **Exact Data Fetching**: Clients can specify exactly which fields they need.
- **Hierarchical Structure**: GraphQL queries mimic the shape of the response.

### Example: GraphQL Query to Fetch User Data

```graphql
{
  user(id: 1) {
    id
    name
    email
    posts {
      title
      content
    }
  }
}
```

## GraphQL vs. REST

| **Feature**            | **GraphQL**                        | **REST**                                        |
|------------------------|------------------------------------|-------------------------------------------------|
| **Data Fetching**       | Fetches only requested fields      | Fetches complete data, potentially over-fetching|
| **Endpoint**            | Single endpoint `/graphql`         | Multiple endpoints for different resources      |
| **Versioning**          | No versioning needed               | Requires new endpoints for each version         |
| **Error Handling**      | Returns partial data along with errors | Typically returns error codes without data    |

