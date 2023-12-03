# ACT_Reservoir
Adaptive Computation Time Applied to Reservoir Networks.

## Abstract
ACT Reservoir embarks on a pioneering journey to establish a neural network architecture that achieves (finite memory) Turing completeness, a milestone made possible through the integration of adaptive computation time (ACT). This project leverages the unique capabilities of ACT, such as halting and flow control, to enable a neural network that can not only process complex tasks but also make decisions about looping and task termination, akin to Turing's conceptual machine.

This novel approach integrates ACT with reservoir computing networks, an unexplored combination that hypothesizes a synergistic relationship between the dense inter-neuronal connections of reservoir networks and the dynamic capabilities of ACT. This combination is anticipated to reflect the complexities of algorithmic language more accurately and enable more intricate representations of variables and their interconnections.

Diverging from traditional reservoir computing methods, ACT_Reservoir innovates by training all weights within the reservoir, emulating aspects of the human brain's adaptability. This not only enhances the network's learning capacity but also aligns more closely with how the human brain processes information. The integration of inputs and outputs directly into the reservoir further strengthens this resemblance, creating a unified and efficient processing system.

As we navigate these new waters, especially in overcoming the challenges of network training, our project is in a state of active exploration and development. We encourage collaboration and input from the broader community, as we advance in this exciting area of AI and neural network research, drawing inspiration from both Turing's theoretical framework and the human brain's architecture.

## Ideas:

1. **Finite Memory Approximation of a Universal Turing Machine**: 
   ACT_Reservoir embodies a "finite memory approximation" of a Universal Turing Machine, as outlined in foundational research (e.g., Siegelmann, 1992). This architecture, when linked with an infinite external memory, has the potential to achieve Turing completeness, demonstrating its vast computational capabilities.

2. **Turing Completeness and Real-World Limitations**: 
   In theory, the architecture could attain Turing completeness even without infinite external memory, provided each weight could assume any rational value (Siegelmann, 1992). However, the practical limitation of finite precision in real-world computational systems constrains this potential, highlighting the gap between theoretical models and practical implementations.

3. **Efficiency in Complex Algorithm Modeling**: 
   Despite the limitations in precision, the network's densely connected, looping structure enables it to model highly complex algorithms, even with a relatively low neuron count. This efficiency suggests that, with a sufficiently large number of neurons, the network could effectively model language, arithmetic, and a variety of tasks, outperforming traditional transformer networks in terms of parameter efficiency. The looping mechanism allows for complex operations with fewer neurons, a notable advancement over existing models.

4. **Global Function Approximation**: 
   Unlike feed-forward networks or even transformers that often focus on local function approximation, ACT_Reservoir aims to build global approximations of functions. This approach allows for a more holistic understanding and representation of the data and processes it is modeling, potentially offering a more robust and versatile framework for neural network applications.

## References
- Siegelmann, H. T. (1992). ["On The Computational Power Of Neural Nets."] (https://binds.cs.umass.edu/papers/1992_Siegelmann_COLT.pdf)
- Graves, A. (2016).  ["Adaptive Computation Time for Recurrent Neural Networks."] (https://arxiv.org/abs/1603.08983)
- Giacomo Bocchese. (2023).["Self Control Reservoir Network: enhancing intelligence for Neural Networks."](https://doi.org/10.5281/zenodo.7637563) (Note: This is a proposal paper and not yet published.)



## Working mechanism
