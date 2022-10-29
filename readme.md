# Relais Control

## Via API
### 1. Install dependiencies
```bash
pip install -r requirements.txt
```

<br>


### 2. Create an object of the control class

```python
serialmanager = SerialManager()
```

<br>

### 3.) Do Actions
#### Get all available USB ports
```python
ports = serialmanager.get_connected_ports()
```

#### Set the state of the port to on or off
```python
serialmanager.set_serial(number=port, on_or_off=state)
```

<br>
<br>

## Via CLI
#### Get the available ports
```bash
python relais.py -a get
```

#### Set the state
```bash
python relais.py -a set -p <Port-Number> -s <State: on | off>
```
