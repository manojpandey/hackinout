from exotel import Exotel 

client = Exotel('non56','eedaef1428bfc46e254134be41cd5380b85ccc56')

from_num = "%011d"% (9560894192) 
call_id  = "%011d"% (9243422233)


x  = client.call_flow(from_num,call_id,(56743))
print x
