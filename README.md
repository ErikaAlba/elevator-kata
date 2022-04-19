# Elevators

## Speciﬁcations

The purpose of this exercise is to model an elevator cluster simulator in a building.

We’ll have in this building n ﬂoors served by x elevators.

Each elevator in the cluster must obey the following rules:

## General Properties

An elevator must serve all pending requests on his way, providing they are in its current direction.

The order of the requests is always the order of the ﬂoors according to the current direction.

The timing of the requests must be taken into account.

If there’s no available elevator to answer a request, the request is cancelled.

The default position for an elevator is the ﬁrst ﬂoor. If an elevator is no more requested, it must then return to the ﬁrst ﬂoor.

## Outside calls

At each ﬂoor — except the ﬁrst one and the last one, the request can be made in two directions. At the ﬁrst ﬂoor, it is only possible to call an elevator to go up and, at the last ﬂoor, it’s only possible to call an elevator to go down.

When a request is made from a ﬂoor, only the nearest elevator going in the direction of the request can answer. If no elevator is currently in use, a default elevator will answer the request.

An elevator cannot answer more than n/x request. If such case arises, another elevator will take over.

## Inside calls
It is not possible to choose a ﬂoor that goes in the opposite direction of the outside call.

## Evaluation

In addition to the necessary class deﬁnitions, a object-oriented style running simulation must be implemented. A CLI-based interface should be enough, but you can provide a more sophisticated interface if you dare

In this exercise, the programming style, good practices, resources used (types, libraries, etc.) will be evaluated, along with any feedback you could make on the statement. The exercise should be performed using only Python, without the need for any other tools, databases or messaging queue managers…