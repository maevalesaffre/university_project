# lesaffre-COO

# UE COO - Project : Project: Self-Service Bicycles

# Member

- Lesaffre Maeva

# Subject
[The subject](https://www.fil.univ-lille.fr/~quinton/coo/projet/competitions.pdf)

We are interested in the design of a simulation of a self-service bicycle rental system.


[UML Project](UML/uml_final.mdj)

# Logbook

## Month 1
The first month was quite empty in the progress of the project, I judged it better to go back to the basics of poo to
finally get up to date so as not to have a project with non-solid foundations. I nevertheless started UML, and made all
the most obvious "mistakes", such as intending to make an enum class for bike types (electric etc). The first month was 
used to think about all the design mistakes not to make.

## Month 2

we think about the uml and we feed it, the project being similar to an L2 poo project, we draw up classes that could be
potentially interesting like BikeStation, Bike. There is not even the idea of ​​an abstract class or a vehicle interface yet,
and the electricalBike classes inherit from Bike which is abstract (not the most optimal...)

Mid-October, we finally have a minimum solid vision, we abandon the enums, we set up a Vehicle, Bike interface which implements
each of the Vehicle functions. As we abandon the enums, we set up the decorator part with the abstractBikeDecorator then 
BasketBikeDecorator and LuggageRackDecorator, the UML for its part is always evolving, corrections, additions and deletions 
(one thing that was missing I think, but that will be discussed in more detail in the conclusion section).

We also set up the Worker and Repairer classes, at the beginning I had the right vision (good code strategy), but afterwards,
there was the mess of integrating the visitor type class and therefore breaking the organization of Worker/Repairer 
subsection. So I kept dynamic Worker => Repairer. And not Visitor <= Person => Worker=> Repairer. This is also the beginning 
of the Strategy coding part, with an AbstractStrategy interface, and the Random and Round Robin Strategy classes, this part 
was quite obvious to link with a design pattern learned in class.


## Month 3
At the beginning of November, bug fixes in the code itself. Then setting up the Interface Observer class, then ControlCenter 
using the Observer design pattern, then modifying the Station class taking Control Center into account, then surely the 
project evolves so that it is solid in terms of its logic and its choices (choosing an interface or abstract class, making 
classes to define a state or just defining it under an attribute, etc.). Then we correct all the code bugs (I don't know why
 but I prefer to do all the classes at the same time one by one, it gives me the impression of revisiting my entire project).

Then we attack the tests and I must admit that this is not my strong point, so the same as for the source code part, we experiment
for the tests. We start with the "simple" classes, Repairer, Strategy classes etc., then Bike, decorated Bikes and finally more complex
sclasses like Station and ControlCenter.

Month of December, we finish the simplest tests, and we tackle the biggest ones (ControlCenter, Station etc), the tests are quite simple
(too simple), the mistake was to look at the main class and simulation at the end, because when thinking about the design of these two
classes I realized that there were missing functions, like putInStation, setting up the User class which corresponds to the individual who 
takes the bike, as he has was created later, it implements Worker (it should be the opposite, hence the confusion on the name of the work() 
method, it should have been called visit(), there was some small feedback on the tests but also on the code (forgetting initialized variables etc).

## CCL, the tests work, the code compiles, executes and respects the project instructions. It could have been more optimal (do more prioritization of 
tests, use the design pattern state).You also have to take into account the fact of being alone but also balancing student work which prevented you 
from coming to class.


### Design pattern part:

## Which Pattern design I used:

#Decorator:
The vehicle management system implements the decorator design pattern to dynamically enrich the functionality of base objects, in this case, 
bicycles. This approach allows additional features to be added to existing bikes without altering their fundamental structure.
The base class, Bike, serves as the foundational component, defining fundamental operations and providing a concrete implementation. Next, 
the abstract class AbstractBikeDecor acts as an abstract decorator, extending Bike while maintaining a reference to a Bike object. This 
abstract class exposes the same methods as the Vehicle interface to ensure compatibility with other system components. Concrete decorator 
classes, such as BasketBicycleDecor, add functionality specific to bicycles. In this case, the capacity of a shopping cart was introduced. 
Each concrete decorator extends AbstractBikeDecor and can be attached to any existing Bike object, thus enriching its functionality.
Using this approach allows for easy and dynamic expansion of bicycle functionality. For example, if we want to add a luggage rack to a bike, 
we simply create a new decorator class, like LuggageRackDecor, and attach it to an existing bike. This avoids any changes to the Bike base class 
and allows scalability without disruption to existing code.

#Observer :
The observer design pattern is applied in the vehicle management system to enable the control center (ControlCenter) to observe the status of 
vehicles and react accordingly. The ControlCenter class acts as an observer, implementing the Observer interface. Each time a vehicle undergoes 
a change of state, the control center is notified, thus triggering the observer's update method. This method then evaluates the condition of the
vehicle and takes appropriate action. When a vehicle is reported as out of service, the control center deploys a repairer to resolve the problem.
This demonstrates the use of the observer model to detect specific events and respond dynamically. The observer also provides the ability to react
to other vehicle status changes, such as when the vehicle is in service or has been stolen. These changes are also handled in the update method, 
illustrating the versatility of this design. The observer design model ensures effective communication between vehicles and the control center, 
enabling proactive and reactive system management. Using this approach, the system can scale to include new vehicle types without requiring 
significant changes to the existing control center code, thus following the open/closed principle of software design. 

#Strategy :
The strategy design model is integrated into the vehicle management system to manage the redistribution of vehicles between different stations.
Two concrete strategies, RandomDistributionStrategy and RoundRobinDistributionStrategy, are implemented to illustrate this flexible approach.
The ControlCenter class uses a redistribution strategy, delegating responsibility for redistribution to an instance of the StrategyDistribution 
interface. This approach makes it possible to dynamically change the redistribution strategy without altering the ControlCenter code, thus 
respecting the open/close principle. The RandomDistributionStrategy strategy uses a random approach to assign vehicles to stations. Each vehicle
in service is assigned to a station at random, thus contributing to an equitable distribution of vehicles. The RoundRobinDistributionStrategy strategy
takes a cyclical approach, successively assigning each vehicle in service to a different station. This ensures a balanced distribution of vehicles between
all stations. Strategies are interchangeable, providing significant flexibility to adapt the system according to changing needs. For example, adding a new
redistribution policy does not involve changes to existing ControlCenter code. Additionally, new strategies can be added without affecting existing classes, 
thus following the Liskov substitution principle.

#Singleton
The ControlCenter class in our vehicle management application is an exemplary example of using the Singleton design pattern. This model ensures that only 
one instance of the class can exist at any given time, providing a centralized point of control throughout the system. First of all, the class's private 
constructor is a key piece of this implementation. By making it private, we prevent unauthorized creation of instances from outside the class. This policy
promotes full control over the creation of ControlCenter objects. Then the static getInstance method is the main input to get a ControlCenter instance. 
It performs a check to see if an instance already exists. If not, it creates a new instance using the private constructor. Otherwise, it simply returns 
the existing instance. This ensures that only one ControlCenter object is present in the entire system.


Java
```
public static ControlCenter getInstance() {
    if (instance == null) {
        instance = new ControlCenter();
    }
    return instance;
}
```

Finally, the static instance variable stores the single instance of ControlCenter. This variable is private, meaning it can only be accessed from inside the 
class. This reinforces the concept of Singleton, as direct access to the instance is limited, ensuring centralized resource management. This implementation of
the Singleton model in the ControlCenter class provides consistent and centralized management of vehicles and stations across our entire application. It promotes
modularity, simplicity, and control, which are fundamental principles of robust software design.

#Visitor:
The Visitor design pattern was used in the design of the Worker, Repairer, and work methods. This pattern makes it possible to define a family of algorithms 
(in this case, the different tasks that workers can perform) without modifying the classes of the elements on which they operate. In our case, the abstract 
Worker class represents a generic worker capable of working on different types of vehicles. The Visitor design pattern is used by declaring the work method 
in the Worker interface and letting the concrete classes (Repairer for example) implement this method specifically for each type of vehicle. So when a worker,
such as a Repairer, visits a specific vehicle, the appropriate work method for that vehicle type is called. This allows new types of workers or new types of 
vehicles to be added without having to modify existing classes, thus following the open/close principle of SOLID.

## Which model I didn't use:

#Factory method:
The Factory Method design pattern is used when one wants to delegate the creation of objects to subclasses, thereby allowing a client class to work with instances 
of subclasses without knowing the details of their creation. I find that creating instances of my specific decorators is not complicated and since I don't need to 
delegate this responsibility to subclasses, I can just continue to create instances directly in the client class without using a Factory Method. Using a Factory 
Method depends on the context and specific requirements of my project. I felt that this didn't make my code simpler or make it more flexible; so I continue to 
create instances directly without using a Factory Method.

#Composite:
same reasoning as for factory method.

#stateWhen designing my vehicle management system, the question of choosing the State design pattern naturally arose. Although the State design pattern offers 
an elegant approach to modeling transitions between different states of an object, I deliberately chose not to implement it in the Vehicle, Bike, and other classes, 
and this choice is based on several considerations specific to our application. One of the main advantages of the State design pattern is its ability to encapsulate 
each state in a separate class, making it easy to add new states without altering existing code. However, in my case, vehicle states were mainly defined by 
boolean properties such as state and offService. I felt that creating a separate class for each state would have introduced unnecessary complexity into the model, 
given that these states are quite simple and do not require complex behaviors. Reading the code would thus be less intuitive, with additional classes for basic states
such as "in service" or "out of service"(if this had attributes other than booleans I would have preferred to adopt the state design pattern).

My choice to stick with Boolean properties to represent states stems from the simplicity and clarity it brings to my code. Transitions between states are handled directly,
without the need to create additional classes. This makes the code more readable and easier to understand, especially for states that don't require specific behaviors.
In conclusion, although the State design pattern is a powerful solution in many cases, my decision not to implement it in these specific classes is based on the principle
of preserving the simplicity and clarity of the code while meeting the specific needs of project.

## How To

### Deposit Recovery
-------------------------
- To get the project you have to fork it from git:

```sh
git clone <adresse du dépôt>
```   
This will create a "lesaffre-coo" folder in the current folder.


- generation of documentation:

```
	javadoc -sourcepath src -d doc -subpackages vehicle main observer strategy worker exceptions


```
- class compilation:

```
	javac -sourcepath src -d classes ./src/main/*.java ./src/exceptions/*.java  ./src/observer/*.java ./src/strategy/*.java ./src/vehicle/*.java ./src/vehicle/bike/*.java ./src/vehicle/bike/bikeDecorator/*.java ./src/exceptions/*.java ./src/worker/*.java


```

- compilation of tests:

```
javac -d classes -classpath ./lib/junit-console.jar ./src/main/*.java ./src/observer/*.java ./src/strategy/*.java ./src/vehicle/*.java ./src/vehicle/bike/*.java ./src/vehicle/bike/bikeDecorator/*.java ./src/exceptions/*.java ./src/worker/*.java ./test/worker/*.java ./test/vehicle/bike/bikeDecorator/*.java ./test/strategy/*.java ./test/observer/*.java
	java -jar ./lib/junit-console.jar -cp classes --scan-classpath --disable-banner


```

-construction of the jar:

```
jar cvfe station_velo.jar main.Main -C classes main -C classes exceptions -C classes vehicle -C classes observer -C classes strategy -C classes worker
	mkdir jar
	mv station_velo.jar jar
```
 
- execution of the jar:

```
	java -jar jar/station_velo.jar

```

- file cleaning:

```
	rm -r doc classes jar

```
 