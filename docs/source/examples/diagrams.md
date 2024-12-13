# Diagrams

Diagrams allow you to visualize concepts and relationships in your documentation using graphical representations. 

The theme supports [Mermaid diagrams](https://mermaid.js.org/) using the [sphinxcontrib-mermaid](https://jbms.github.io/sphinx-immaterial/mermaid_diagrams.html) extension, which provides an easy way to generate various types of diagrams.

## Example

### Flowchart

```md
:::{mermaid} 
:name: flowchart
graph LR
    A[Start] --> B{Error?};
    B -->|Yes| C[Hmm...];
    C --> D[Debug];
    D --> B;
    B ---->|No| E[Yay!];
:::
```

Renders:

:::{mermaid} 
:name: flowchart
graph LR
    A[Start] --> B{Error?};
    B -->|Yes| C[Hmm...];
    C --> D[Debug];
    D --> B;
    B ---->|No| E[Yay!];
:::

### Sequence diagram

```md
:::{mermaid} 
:name: sequence-diagram
sequenceDiagram
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
:::
```

Renders:

:::{mermaid} 
:name: sequence-diagram
sequenceDiagram
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
:::

### Class diagram

```md
:::{mermaid} 
:name: class-diagram
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
:::
```

Renders:

:::{mermaid} 
:name: class-diagram
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
:::

## See also

- [sphinxcontrib-mermaid](https://jbms.github.io/sphinx-immaterial/mermaid_diagrams.html)
- [Mermaid diagrams](https://mermaid.js.org/)
