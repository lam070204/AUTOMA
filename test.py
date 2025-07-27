from mpu6050 import mpu6050

mpu = mpu6050(0x68, bus=0)  # Bus 0 là I2C0

print("Nhiệt độ:", mpu.get_temp())
print("Gia tốc:", mpu.get_accel_data())
print("Gyro:", mpu.get_gyro_data())
