# ACT_Reservoir
Adaptive Computation Time Applied to Reservoir Networks.
It's an extension of my other work : [Self Control Reservoir Network](https://github.com/BoccheseGiacomo/SCRN----Pre-Alpha-version)

Since i discovered that with that work i re-invented the ACT paradigm in a totally independent way, and after discovering the close similarities of the work of A.Graves on ACT i decided to put that name to my work rather then SCRN and merging a bit the functionalities.

*Please note that this project is still in development phase and that many claims I make comes from theoretical and intuitive considerations rather than experimental results.*

## Abstract
ACT Reservoir is an explorative project aimed at developing a neural network architecture with the potential for (finite memory) Turing completeness. This endeavor is made possible by integrating Adaptive Computation Time (ACT). The project utilizes the distinctive features of ACT, including halting and flow control, to allow simpler and more global representations of modeled functions. This approach draws inspiration from Turing's theoretical framework, aiming to implement these principles in a practical, modern neural network context.

This novel approach integrates ACT with reservoir computing networks, an unexplored combination that hypothesizes a synergistic relationship between the dense inter-neuronal connections of reservoir networks and the dynamic capabilities of ACT. This combination is anticipated to reflect the complexities of algorithmic language more accurately and enable more intricate representations of variables and their interconnections.

Diverging from traditional reservoir computing methods, ACT_Reservoir innovates by training all weights within the reservoir, emulating aspects of the human brain's adaptability. This not only enhances the network's learning capacity but also aligns more closely with how the human brain processes information. The integration of inputs and outputs directly into the reservoir further strengthens this resemblance, creating a unified and efficient processing system. (the standard layer-based approach with forward propagation i think intrinsecly limits the behaviours of an ANN).

As we navigate these new waters, especially in overcoming the challenges of network training, our project is in a state of active exploration and development (expecially it's very hard to train). We encourage collaboration and input from the broader community, as we advance in this exciting area of AI and neural network research, drawing inspiration from both Turing's theoretical framework and the human brain's architecture.

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
- Siegelmann, H. T. (1992). ["On The Computational Power Of Neural Nets."](https://binds.cs.umass.edu/papers/1992_Siegelmann_COLT.pdf)
- Graves, A. (2016).  ["Adaptive Computation Time for Recurrent Neural Networks."](https://arxiv.org/abs/1603.08983)
- Giacomo Bocchese (2023). ["Self Control Reservoir Network: enhancing intelligence for Neural Networks."](https://doi.org/10.5281/zenodo.7637563) (Note: This is a draft proposal paper, not reviewed, yet to be optimized and not yet published)



## Working mechanism
The ACT_reservoir class implements a neural network model that integrates adaptive computation time (ACT) within a reservoir computing framework. The network is characterized by its ability to dynamically adjust its computational depth based on the input data.

Upon initialization, the network is configured with specific dimensions for input, hidden, and output layers, and a predefined maximum number of iterations. The architecture includes a bias unit for offset adjustments and a halting unit to control the iteration process.

The core computational process occurs in the *predict* method. Here, the network takes an input vector, initializes a state vector that represents the current state of the network, and iterates through computational steps. At each step, the network's state is updated by applying the ReLU activation function to the matrix product of the network's weights and the current state. This process is repeated until a defined halting condition is met, which is determined by the value in the halting unit of the state vector.

![image](https://github.com/BoccheseGiacomo/ACT_Reservoir/assets/104854120/0dab7915-1846-4e4d-9db4-1c53b37b7daa)



The state vector is divided into segments corresponding to the input, hidden, and output layers. The network's output is extracted from the relevant segment of the state vector upon completion of the iteration process.

### There are three versions of the file:

-The task i'm teaching it is integer multiplication.

-**act_reservoir.py** -> class of the network implementation

-**act_reservoir_backprop.ipynb** -> includes an implementation of backprop to try to train it (not properly working, i think)

-**act_reservoir_zeroth.ipynb** -> tries to optimize weights with zeroth order opt. algorithms (more indicated for this task)
