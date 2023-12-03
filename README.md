# ACT_Reservoir
Adaptive Computation Time Applied to Reservoir Networks.

## Abstract
ACT Reservoir embarks on a pioneering journey to establish a neural network architecture that achieves (finite memory) Turing completeness, a milestone made possible through the integration of adaptive computation time (ACT). This project leverages the unique capabilities of ACT, such as halting and flow control, to enable a neural network that can not only process complex tasks but also make decisions about looping and task termination, akin to Turing's conceptual machine.

This novel approach integrates ACT with reservoir computing networks, an unexplored combination that hypothesizes a synergistic relationship between the dense inter-neuronal connections of reservoir networks and the dynamic capabilities of ACT. This combination is anticipated to reflect the complexities of algorithmic language more accurately and enable more intricate representations of variables and their interconnections.

Diverging from traditional reservoir computing methods, ACT_Reservoir innovates by training all weights within the reservoir, emulating aspects of the human brain's adaptability. This not only enhances the network's learning capacity but also aligns more closely with how the human brain processes information. The integration of inputs and outputs directly into the reservoir further strengthens this resemblance, creating a unified and efficient processing system.

As we navigate these new waters, especially in overcoming the challenges of network training, our project is in a state of active exploration and development. We encourage collaboration and input from the broader community, as we advance in this exciting area of AI and neural network research, drawing inspiration from both Turing's theoretical framework and the human brain's architecture.

## Ideas and references to literature:
-It's already provent that such architecture represents a "finite memory approximation" of an Universal Turing Machine. If linked to an infinite external memory this can achieve turing completeness.
-In reality, this architecture would be turing complete even without infinite external memory, but with the assumption that every rational value could be attribuited to weights, in the real world we have finite precision numbers so this would be impossible in practice.
-Anyway, even with a low number of neurons this network would be able to model very complex algorithms, due to the dense and looping inter-neuronal connections. So with a sufficiently high number of neurons it can be used to model language, arithmetics and any kind of task, and the required number of parameters would be much lower than transformer networks since by using looping we can perform complex operations with less neurons.
-This network tries to build global approximation of function, not only local ones like in feed-forward networks or even transformers without external context.

-> https://binds.cs.umass.edu/papers/1992_Siegelmann_COLT.pdf [On The Computational Power Of Neural Nets]
-> https://arxiv.org/abs/1603.08983 [Adaptive Computation Time for Recurrent Neural Networks]
-> https://doi.org/10.5281/zenodo.7637563 [Self Control Reservoir Network : enhancing intelligence for Neural Networks] (this is only a proposal paper, not published)


## Working mechanism
