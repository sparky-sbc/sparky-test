��debug fs �򿪵�����£���ϵͳ�����и�Ŀ¼ dmm
/sys/kernel/debug/dmm/
  	enable
	master0
	   id 
	   mode
	master1
	   id 
	   mode
	max_statistic_cnt
	result
	sampling_rate
	statistic_cnt
	
enable: ��ʼ������ֹͣͳ�� 
      ��ʼͳ�� echo 1 > enable 
      ֹͣͳ�� echo 0 > enable 
      
master0 �� master1 �ֱ�����Ҫͳ�Ƶ�����master ��Ϣ

id ����ѡ��ID ��ʱ�� ��Ҫ���ݴ�ֵ��������
	MASTER_ID_CPU = 0,
	MASTER_ID_USB3,
	MASTER_ID_VCE,
	MASTER_ID_ENTHERNET,
	MASTER_ID_USB2,
	MASTER_ID_DE,
	MASTER_ID_GPU3D,
	MASTER_ID_SI,
	MASTER_ID_DMA,
	MASTER_ID_DAP,
	MASTER_ID_ALL,
	MASTER_ID_IDLE,
	
mode ����ѡ��MODE  ��ʱ�� ��Ҫ���ݴ�ֵ��������
	MASTER_MODE_READ = 0,   // ͳ�ƶ�
	MASTER_MODE_WRITE, //ͳ��д
	MASTER_MODE_ALL, //ͳ�ƶ�д

����ͨ���������޸���Ҫͳ�Ƶ�master ��ͳ�Ƶ�ģʽ

max_statistic_cnt�� ����ܹ�ͳ�ƵĴ�����ֻҪ���ڴ����ơ�Ĭ����1000�Σ�����ͨ��echo 2000 > max_statistic_cnt ���޸�

sampling_rate�������ļ��ʱ�䣬 Ĭ����1s ͳ��һ�Σ�Ҳ����ͨ��echo 2000 > sampling_rate �޸ġ�

statistic_cnt����ǰͳ���˶��ٴΣ�ֻ����ͨ��cat statistic_cnt ��ȡ

result:ͳ�ƵĽ����ֻ�� ͨ��cat result ��ȡ
���˵����
       master id:   mode   bandwidth(M byte)     percent of total(%)        master id:   mode   bandwidth(M byte)    percent of total(%)
             ALL:    RW               400                         13            IDLE:    RW               433                         85 
             ALL:    RW               612                         21            IDLE:    RW              1178                         60 
             ALL:    RW               714                         24            IDLE:    RW               989                         66 
             ALL:    RW               616                         21            IDLE:    RW              1165                         60 
             ALL:    RW               635                         22            IDLE:    RW              1128                         61 
             ALL:    RW               667                         23            IDLE:    RW              1067                         63 
             ALL:    RW               625                         21            IDLE:    RW              1145                         61 
             ALL:    RW               655                         22            IDLE:    RW              1096                         62 
             ALL:    RW               649                         22            IDLE:    RW              1110                         62 
master id : ָͳ�Ƶ����Ǹ�master �磺 all �������е�master ��IDLE ��ʾͳ��DDR IDEL ��ʱ��
MODE �� ָ��ͳ�Ƶ�ģʽ�� R ��W �� RW ��3��ģʽ
bandwidth��ͳ�Ƶ�master��ָ��ʱ���ڵĴ���M Ϊ��λ 400M byte
percent of total�� ͳ�Ƶİٷֱȣ��ǵ�ǰmaster �Ĵ����ϵͳ�����ܴ���ıȣ� IDLE �Ǹ����⣬��ͳ��IDLE��ʱ�򣬴�ʱ�İٷֱȻ���Ϊ�˷�IDLE��cycle ��ϵͳDDR�ܵ�cycle ֮��ı���

ʹ�����̣�
1.������ز���
2.��ʼͳ�� 
3.ֹͣͳ��
4.�鿴���
  
  
�磺��Ҫͳ��DE �Ĵ����GPU�Ĵ�����������2s����һ�Σ����ͳ�ƴ���Ϊ 500��
echo 5 > /sys/kernel/debug/dmm/master0/id 
echo 0 > /sys/kernel/debug/dmm/master0/mode 
echo 6 > /sys/kernel/debug/dmm/master1/id
echo 2 > /sys/kernel/debug/dmm/master1/mode

echo 2000 > /sys/kernel/debug/dmm/sampling_rate
echo 500 > /sys/kernel/debug/dmm/max_statistic_cnt

echo 1 > /sys/kernel/debug/dmm/enable
����UI һ��ʱ���
������������
echo 0 > /sys/kernel/debug/dmm/enable

cat /sys/kernel/debug/dmm/result > /data/result.txt
�鿴���



Ĭ�������ͳ�Ƶ��� ����master �Ĵ���� IDLE ���������������1s �����ͳ�ƴ�����1000��

�磺 
echo 1 > /sys/kernel/debug/dmm/enable
����UI һ��ʱ���
������������
echo 0 > /sys/kernel/debug/dmm/enable

cat /sys/kernel/debug/dmm/result > /data/result.txt  ���ǰ��������Ĭ�����ý���ͳ�ơ�
