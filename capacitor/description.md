# Basic

## RC circuit

A **resistor–capacitor circuit** (**RC circuit**), or **RC filter** or **RC network**, is an electric circuit composed of resistors and capacitors.

![img](images/200px-Discharging_capacitor.svg.png)

## RC time constant

The **RC time constant**, also called tau, the **time constant (in seconds)** of an RC circuit, is equal to the product of the **circuit resistance (in ohms)** and the circuit **capacitance (in farads)**, i.e.
$$
\tau =RC
$$

## Charging

Charging toward applied voltage (initially zero voltage across capacitor, constant $V_0$ across resistor and capacitor together) $V_0$:
$$
V(t)=V_0(1-e^{-t/\tau})
$$

## Discharging

Discharging toward zero from initial voltage (initially $V_0$ across capacitor, constant zero voltage across resistor and capacitor together) $V_0$:
$$
V(t)=V_0(e^{-t/\tau})
$$


# Equivalent resistance of MCU

We first give the **maximum current (in $\mu\text{A}$)** that each development board running the testbench at different frequency (MCLK & SMCLK) (**constant power supply, ADC does not run**):

| Frequency     | FR5994 (in $\mu\text{A}$) | FR5969 (in $\mu\text{A}$) | FR2433 (in $\mu\text{A}$) |
| ------------- | :-----------------------: | ------------------------- | ------------------------- |
| $1\text{MHz}$ |          $465.4$          | /                         | /                         |
| $2\text{MHz}$ |          $677.7$          | /                         | /                         |
| $4\text{MHz}$ |         $1062.4$          | /                         | /                         |
| $8\text{MHz}$ |         $1879.1$          | /                         | /                         |

