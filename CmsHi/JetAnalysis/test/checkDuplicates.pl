#!/usr/bin/perl

@files = `srmls -2 "srm://srm-dcache.rcac.purdue.edu:8443/srm/v2/server?SFN=/mnt/hadoop/store/user/kjung/pPb_BForest" | grep .root`;
chomp(@files);
my ( $counter ) = 0;
my ( $lastretryno );
my ( $lastjobno );

foreach $ifile (@files){
    $counter++;
        
    my ( $jobno ) = $ifile =~ m/(\d+)(?!.*d)/i;
    my ( $retryno ) = $ifile =~ m/(\d+)(?!.*\d)/i;
    
    if (($jobno==$lastjobno) && ($jobno > 250)){
        print "jobno: $jobno\n";
        print "retryno: $retryno\n";
    }
    else{
        $lastretryno = $retryno;
        $lastjobno = $jobno;
    }
}
