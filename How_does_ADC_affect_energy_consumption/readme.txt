● 'rawdata.yaml'包含了在constant power supply下，MSP430FR5994、MSP430FR5969、MSP430FR2433三个开发板在1MHz、2MHz、4MHz下，ADC采样间隔从100us到1000us以及不进行ADC采样时，系统空闲和运行testbench下的电流消耗（单位为mA，电流值从左到右分别为[mean, min, max]）。
● 'ADC_sample_frequency_vs_extra_current'分析了ADC的采样频率与额外电流的关系，为后续计算合理的ADC采样间隔做准备。
● 'Ratio_of_extra_current_of_the_ADC'分析了ADC的额外电流与开发板本身电流的比值。
● 'Formula_derivation_of_ADC_sampling_interval'利用上面的信息尝试对ADC sample interval做出一个reasonable的计算公式。

【NOTE】
电流消耗测量通过Energy Trace完成。（见：https://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_energytrace.html）
.mlx需要Matlab 2021以上版本的支持。（见：https://ww2.mathworks.cn/help/matlab/matlab_prog/live-script-file-format.html?requestedDomain=cn）
.ipynb需要anaconda和Jupyter的支持。（anaconda见：https://www.anaconda.com/，Jupyter见https://jupyter.org/）