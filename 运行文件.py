import wx
import CAPPING
# Implementing MyFrame1
class MyProject1MyFrame1( CAPPING.MyFrame1 ):
	def __init__( self, parent ):
		CAPPING.MyFrame1.__init__( self, parent )
	
	# Handlers for MyFrame1 events.
	def JI( self, event ):
         xulie=str(self.Xulie.GetValue())
         ATP=xulie.count("A")
         UTP=xulie.count("U")
         TTP=xulie.count("T")
         CTP=xulie.count("C")
         GTP=xulie.count("G")
         UTP=UTP+TTP
         C=ATP*10+UTP*9+GTP*10+CTP*9
         H=ATP*12+UTP*11+GTP*12+CTP*12
         N=ATP*5+UTP*2+GTP*5+CTP*3
         O=ATP*6+UTP*8+GTP*7+CTP*7
         P=ATP*1+UTP*1+GTP*1+CTP*1
         HM=1.00782503
         NM=14.00307401
         CM=12
         OM=15.99491462
         PM=30.97376149
         CM1=12.01073590219
         NM1=14.0067032158057
         HM1=1.00794075182625
         OM1=15.9994049263486
         PM1=30.97376149
         DE=1.0073
         OH=C*CM+(H+1)*HM+N*NM+(O-2)*OM+(P-1)*PM-DE
         MONO=C*CM+(H+2)*HM+N*NM+(O+1)*OM+P*PM-DE
         DI=C*CM+(H+3)*HM+N*NM+(O+4)*OM+(P+1)*PM-DE
         TRI=C*CM+(H+4)*HM+N*NM+(O+7)*OM+(P+2)*PM-DE
         GCAP=(C+10)*CM+(H+16)*HM+(N+5)*NM+(O+11)*OM+(P+2)*PM-DE
         CAP0=(C+11)*CM+(H+18)*HM+(N+5)*NM+(O+11)*OM+(P+2)*PM-DE
         CAP1=(C+12)*CM+(H+20)*HM+(N+5)*NM+(O+11)*OM+(P+2)*PM-DE
         OH1=C*CM1+(H+1)*HM1+N*NM1+(O-2)*OM1+(P-1)*PM1-DE
         MONO1=C*CM1+(H+2)*HM1+N*NM1+(O+1)*OM1+P*PM1-DE
         DI1=C*CM1+(H+3)*HM1+N*NM1+(O+4)*OM1+(P+1)*PM1-DE
         TRI1=C*CM1+(H+4)*HM1+N*NM1+(O+7)*OM1+(P+2)*PM1-DE
         GCAP1=(C+10)*CM1+(H+16)*HM1+(N+5)*NM1+(O+11)*OM1+(P+2)*PM1-DE
         CAP01=(C+11)*CM1+(H+18)*HM1+(N+5)*NM1+(O+11)*OM1+(P+2)*PM1-DE
         CAP11=(C+12)*CM1+(H+20)*HM1+(N+5)*NM1+(O+11)*OM1+(P+2)*PM1-DE
         OH1=round(OH1,8)
         MONO1=round(MONO1,8)
         DI1=round(DI1,8)
         TRI1=round(TRI1,8)
         GCAP1=round(GCAP1,8)
         CAP01=round(CAP01,8)
         CAP11=round(CAP11,8)
         OH=round(OH,8)
         MONO=round(MONO,8)
         DI=round(DI,8)
         TRI=round(TRI,8)
         GCAP=round(GCAP,8)
         CAP0=round(CAP0,8)
         CAP1=round(CAP1,8)
         self.OH.SetValue(str(OH))
         self.MONO.SetValue(str(MONO))
         self.DI.SetValue(str(DI))
         self.TRI.SetValue(str(TRI))
         self.GCAP.SetValue(str(GCAP))
         self.CAP0.SetValue(str(CAP0))
         self.CAP1.SetValue(str(CAP1))
         self.OH1.SetValue(str(OH1))
         self.MONO1.SetValue(str(MONO1))
         self.DI1.SetValue(str(DI1))
         self.TRI1.SetValue(str(TRI1))
         self.GCAP1.SetValue(str(GCAP1))
         self.CAP01.SetValue(str(CAP01))
         self.CAP11.SetValue(str(CAP11))    
if __name__== '__main__':
    app = wx.App(False)
    frame = MyProject1MyFrame1(None)
    frame.Show(True)
    app.MainLoop()
	
	
