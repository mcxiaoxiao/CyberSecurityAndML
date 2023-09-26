# CyberSecurityAndML
机器学习和安全相关的一些小东西

# ML Model Watermarking
https://github.com/SAP/ml-model-watermarking
用于给模型添加隐藏且不可移除的的数字水印，而无需理解底层概念。不会对模型的准确性产生显著降低。有助于保护模型的知识产权，及时发现恶意使用或侵权行为。
支持Scikit-learn, Pytorch , Tensorflow
（工具参考了动态对抗水印的paper但是示例代码中不知道体现在哪 可能确实没有 水印在模型训练时嵌入,而非在预测时动态添加）
  
# ZOO Attack
https://github.com/IBM/ZOO-Attack ZOO（Zeroth Order Optimization based Black-box Attacks to Deep Neural Networks）是一种基于零阶优化的黑盒攻击方法，用于攻击深度神经网络（DNN）。它提出了一种高效的黑盒攻击方法，只需要访问目标DNN的输入（图像）和输出（置信度分数），使攻击更加高效。该方法不需要迁移学习或生成替代模型。
