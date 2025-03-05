# Diagrams

Diagrams allow you to visualize concepts and relationships in your documentation using graphical representations. 

The theme supports [Mermaid diagrams](https://mermaid.js.org/) using the [sphinx-immaterial](https://jbms.github.io/sphinx-immaterial/mermaid_diagrams.html) extension, which provides an easy way to generate various types of diagrams.

## Example

### Flowchart

```{md-mermaid}
:name: flowchart
graph LR
    A[Start] --> B{Error?};
    B -->|Yes| C[Hmm...];
    C --> D[Debug];
    D --> B;
    B ---->|No| E[Yay!];
```

### Sequence diagram

```{md-mermaid}
    sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
```

### Class diagram

```{md-mermaid}
classDiagram
    Person <|-- Student
    Person <|-- Professor
    Person : +String name
    Person : +String phoneNumber
    Person : +String emailAddress
    Person: +purchaseParkingPass()
    Address "1" <-- "0..1" Person:lives at
    class Student{
        +int studentNumber
        +int averageMark
        +isEligibleToEnrol()
        +getSeminarsTaken()
    }
    class Professor{
        +int salary
    }
    class Address{
        +String street
        +String city
        +String state
        +int postalCode
        +String country
        -validate()
        +outputAsLabel()
    }
```
