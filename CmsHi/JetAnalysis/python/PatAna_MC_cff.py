import FWCore.ParameterSet.Config as cms

# Pat 
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *



# Photons

makeHeavyIonPhotons.remove(interestingTrackEcalDetIds)
photonMatch.matched = cms.InputTag("hiGenParticles")

patPhotons.addPhotonID = cms.bool(False)
makeHeavyIonPhotons *= selectedPatPhotons


# Jets


patJets.jetSource  = cms.InputTag("iterativeConePu5CaloJets")
patJets.addBTagInfo         = True
patJets.addTagInfos         = True
patJets.addDiscriminators   = True
patJets.addAssociatedTracks = True
patJets.addJetCharge        = False
patJets.addJetID            = True
patJets.getJetMCFlavour     = True #true for MC - fills refparton_flavorForB
patJets.addGenPartonMatch   = True #true for MC - fills refparton_flavor
patJets.addGenJetMatch      = True #true for MC
patJets.embedGenJetMatch    = True
patJets.embedGenPartonMatch = True
patJets.embedCaloTowers	    = False

patJetCorrFactors.useNPV = False
# full reco

#icPu5patJets = patJets.clone(
#  jetSource = cms.InputTag("iterativeConePu5CaloJets"),
#  genJetMatch = cms.InputTag("icPu5match"),
#  genPartonMatch = cms.InputTag("icPu5parton"),
#  jetCorrFactorsSource = cms.VInputTag(cms.InputTag("icPu5corr"))
#  )
icPu5corr    = patJetCorrFactors.clone(src      = cms.InputTag("iterativeConePu5CaloJets"),
                                       levels   = cms.vstring('L2Relative','L3Absolute'),
                                       payload  = cms.string('IC5Calo_2760GeV'))

akPu5PFcorr = icPu5corr.clone(
  src = cms.InputTag("akPu5PFJets"),
  #payload = cms.string('AK5PF_hiIterativeTracks')
  )
akPu5PFpatJets = patJets.clone(
  jetSource = cms.InputTag("akPu5PFJets"),
  genJetMatch = cms.InputTag("akPu5PFmatch"),
  genPartonMatch = cms.InputTag("akPu5PFparton"),
  jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5PFcorr"))
  )

akPu3PFcorr = icPu5corr.clone()
akPu3corr = icPu5corr.clone()

#akPu3PFcorr = icPu5corr.clone(
#  src = cms.InputTag("akPu3PFJets"),
#  payload = cms.string('AK3PF_hiIterativeTracks')
#  )

#akPu3PFpatJets = patJets.clone(
#  jetSource = cms.InputTag("akPu3PFJets"),
#  genJetMatch = cms.InputTag("akPu3PFmatch"),
#  genPartonMatch = cms.InputTag("akPu3PFparton"),
#  jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr"))
#  )

#akPu5corr = icPu5corr.clone(
#    src = cms.InputTag("akPu5CaloJets"),
#    payload = cms.string('AK5Calo')
#    )

#akPu5patJets = patJets.clone(
#    jetSource = cms.InputTag("akPu5CaloJets"),
#    genJetMatch = cms.InputTag("akPu5match"),
#    genPartonMatch = cms.InputTag("akPu5parton"),
#    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5corr"))
#    )

#akPu3corr = icPu5corr.clone(
#    src = cms.InputTag("akPu3CaloJets"),
#    payload = cms.string('AK5Calo')
#    )

#akPu3patJets = patJets.clone(
#    jetSource = cms.InputTag("akPu3CaloJets"),
#    genJetMatch = cms.InputTag("akPu3match"),
#    genPartonMatch = cms.InputTag("akPu3parton"),
#    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3corr"))
#    )



# mc matching
patJetPartonMatch.matched = cms.InputTag("hiPartons")

icPu5clean = heavyIonCleanedGenJets.clone( src = cms.InputTag('iterativeCone5HiGenJets') )
icPu5match = patJetGenJetMatch.clone(
  src = cms.InputTag("iterativeConePu5CaloJets"),
  matched = cms.InputTag("icPu5clean")
  )
icPu5parton = patJetPartonMatch.clone(
  src = cms.InputTag("iterativeConePu5CaloJets")
	)


akPu5PFclean = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak5HiGenJets') ) 
akPu5PFmatch = patJetGenJetMatch.clone(
  src = cms.InputTag("akPu5PFJets"),
  matched = cms.InputTag("akPu5PFclean")
  )
akPu5PFparton = patJetPartonMatch.clone(
  src = cms.InputTag("akPu5PFJets")
	)

akPu3PFclean = heavyIonCleanedGenJets.clone( src = cms.InputTag('ak3HiGenJets') ) 
akPu3PFmatch = patJetGenJetMatch.clone(
  src = cms.InputTag("akPu3PFJets"),
  matched = cms.InputTag("akPu3PFclean")
  )
akPu3PFparton = patJetPartonMatch.clone(
  src = cms.InputTag("akPu3PFJets")
	)

akPu5match = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu5CaloJets"),
    matched = cms.InputTag("akPu5PFclean")
    )
akPu5parton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu5CaloJets")
    )

akPu3match = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu3CaloJets"),
    matched = cms.InputTag("akPu3PFclean")
    )
akPu3parton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu3CaloJets")
    )

from RecoJets.JetAssociationProducers.ak5JTA_cff import *
from RecoBTag.Configuration.RecoBTag_cff import *
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ calo jet
#### b-tagging:
# b-tagging general configuration
# @@@@@@@@@ calo jet
#### b-tagging:
# b-tagging general configuration
icPu5JetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
icPu5JetTracksAssociatorAtVertex.jets   = cms.InputTag("iterativeConePu5CaloJets")
icPu5JetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")

# impact parameter b-tag
icPu5ImpactParameterTagInfos                = impactParameterTagInfos.clone()
icPu5ImpactParameterTagInfos.jetTracks      = cms.InputTag("icPu5JetTracksAssociatorAtVertex")
icPu5ImpactParameterTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")

icPu5TrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
icPu5TrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("icPu5ImpactParameterTagInfos"))
icPu5TrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
icPu5TrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("icPu5ImpactParameterTagInfos"))
icPu5JetProbabilityBJetTags                = jetProbabilityBJetTags.clone()
icPu5JetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("icPu5ImpactParameterTagInfos"))
icPu5JetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
icPu5JetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("icPu5ImpactParameterTagInfos"))

# secondary vertex b-tag
icPu5SecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
icPu5SecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("icPu5ImpactParameterTagInfos")
icPu5SimpleSecondaryVertexBJetTags               = simpleSecondaryVertexBJetTags.clone()
icPu5SimpleSecondaryVertexBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("icPu5SecondaryVertexTagInfos"))
icPu5CombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
icPu5CombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("icPu5ImpactParameterTagInfos"),
                                                                         cms.InputTag("icPu5SecondaryVertexTagInfos"))
icPu5CombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
icPu5CombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("icPu5ImpactParameterTagInfos"),
                                                                         cms.InputTag("icPu5SecondaryVertexTagInfos"))

# soft muon b-tag
icPu5SoftMuonTagInfos                = softMuonTagInfos.clone()
icPu5SoftMuonTagInfos.jets           = cms.InputTag("iterativeConePu5CaloJets")
icPu5SoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
icPu5SoftMuonBJetTags                = softMuonBJetTags.clone()
icPu5SoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("icPu5SoftMuonTagInfos"))
icPu5SoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
icPu5SoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("icPu5SoftMuonTagInfos"))
icPu5SoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
icPu5SoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("icPu5SoftMuonTagInfos"))

# ghost tracks
icPu5GhostTrackVertexTagInfos                 = ghostTrackVertexTagInfos.clone()
icPu5GhostTrackVertexTagInfos.trackIPTagInfos = cms.InputTag("icPu5ImpactParameterTagInfos")
icPu5GhostTrackBJetTags                       = ghostTrackBJetTags.clone()
icPu5GhostTrackBJetTags.tagInfos              = cms.VInputTag(cms.InputTag("icPu5ImpactParameterTagInfos"),
                                                                      cms.InputTag("icPu5GhostTrackVertexTagInfos"))
# prepare a path running the new modules
icPu5JetTracksAssociator = cms.Sequence(icPu5JetTracksAssociatorAtVertex)
icPu5JetBtaggingIP       = cms.Sequence(icPu5ImpactParameterTagInfos * (icPu5TrackCountingHighEffBJetTags +
                                                                                        icPu5TrackCountingHighPurBJetTags +
                                                                                        icPu5JetProbabilityBJetTags +
                                                                                        icPu5JetBProbabilityBJetTags
                                                                                        )
                                                )

icPu5JetBtaggingSV = cms.Sequence(icPu5ImpactParameterTagInfos *
                                          icPu5SecondaryVertexTagInfos * (icPu5SimpleSecondaryVertexBJetTags +
                                                                                  icPu5CombinedSecondaryVertexBJetTags +
                                                                                  icPu5CombinedSecondaryVertexMVABJetTags
                                                                                  )
                                          +icPu5GhostTrackVertexTagInfos
                                          *icPu5GhostTrackBJetTags
                                          )


icPu5JetBtaggingMu = cms.Sequence(icPu5SoftMuonTagInfos * (icPu5SoftMuonBJetTags +
                                                                           icPu5SoftMuonByIP3dBJetTags +
                                                                           icPu5SoftMuonByPtBJetTags
                                                                           )
                                          )

icPu5JetBtagging = cms.Sequence(icPu5JetBtaggingIP 
                                        *icPu5JetBtaggingSV 
                                        *icPu5JetBtaggingMu
                                        )
#----------------------


#----------------------

icPu5clean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('iterativeCone5HiGenJets')) # cleans the jets, but NOT the partons
icPu5match   = patJetGenJetMatch.clone(src      = cms.InputTag("iterativeConePu5CaloJets"),
                                                       matched  = cms.InputTag("icPu5clean"))

icPu5parton  = patJetPartonMatch.clone(src      = cms.InputTag("iterativeConePu5CaloJets"))

# ----- flavour bit
icPu5PatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("iterativeConePu5CaloJets"),
                                                                                   partons = cms.InputTag("genPartons"),
                                                                                   coneSizeToAssociate = cms.double(0.4))
icPu5PatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("icPu5PatJetPartonAssociation"))

icPu5PatJetFlavourId               = cms.Sequence(icPu5PatJetPartonAssociation*icPu5PatJetFlavourAssociation)

#-------

icPu5patJets = patJets.clone(jetSource            = cms.InputTag("iterativeConePu5CaloJets"),
                                             genJetMatch          = cms.InputTag("icPu5match"),
                                             genPartonMatch       = cms.InputTag("icPu5parton"),
                                             jetCorrFactorsSource = cms.VInputTag(cms.InputTag("icPu5corr")),
                                             JetPartonMapSource   = cms.InputTag("icPu5PatJetFlavourAssociation"),
                                             trackAssociationSource = cms.InputTag("icPu5JetTracksAssociatorAtVertex"),
                                             discriminatorSources = cms.VInputTag(cms.InputTag("icPu5CombinedSecondaryVertexBJetTags"),
                                                                                  cms.InputTag("icPu5CombinedSecondaryVertexMVABJetTags"),
                                                                                  cms.InputTag("icPu5JetBProbabilityBJetTags"),
                                                                                  cms.InputTag("icPu5JetProbabilityBJetTags"),
                                                                                  cms.InputTag("icPu5SoftMuonByPtBJetTags"),                
                                                                                  cms.InputTag("icPu5SoftMuonByIP3dBJetTags"),
                                                                                  cms.InputTag("icPu5TrackCountingHighEffBJetTags"),
                                                                                  cms.InputTag("icPu5TrackCountingHighPurBJetTags"),
                                                                                  ),
                                             )


#### B-tagging for this bit:
# b-tagging general configuration
akPu3PFJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
akPu3PFJetTracksAssociatorAtVertex.jets   = cms.InputTag("akPu3PFJets")
akPu3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag
akPu3PFImpactParameterTagInfos               = impactParameterTagInfos.clone()
akPu3PFImpactParameterTagInfos.jetTracks     = cms.InputTag("akPu3PFJetTracksAssociatorAtVertex")
akPu3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu3PFTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
akPu3PFTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
akPu3PFTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
akPu3PFTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
akPu3PFJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()
akPu3PFJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
akPu3PFJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
akPu3PFJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))

#negative impact parameter
from RecoBTag.ImpactParameter.positiveOnlyJetProbabilityComputer_cfi import *
from RecoBTag.ImpactParameter.positiveOnlyJetProbabilityJetTags_cfi import *
from RecoBTag.ImpactParameter.negativeOnlyJetProbabilityComputer_cfi import *
from RecoBTag.ImpactParameter.negativeOnlyJetProbabilityJetTags_cfi import *
#from RecoBTag.ImpactParameterLearning.negativeTrackCountingHighPurJetTags_cfi import *
from RecoBTag.ImpactParameter.negativeTrackCountingHighEffJetTags_cfi import *
from RecoBTag.ImpactParameter.negativeTrackCountingHighPur_cfi import *
from RecoBTag.ImpactParameter.positiveOnlyJetBProbabilityComputer_cfi import *
from RecoBTag.ImpactParameter.positiveOnlyJetBProbabilityJetTags_cfi import *
from RecoBTag.ImpactParameter.negativeOnlyJetBProbabilityComputer_cfi import *
from RecoBTag.ImpactParameter.negativeOnlyJetBProbabilityJetTags_cfi import *

akPu3PFPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()  
akPu3PFNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()    
akPu3PFNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()  
akPu3PFNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()         
akPu3PFNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
akPu3PFPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

akPu3PFPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
akPu3PFNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
akPu3PFNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
akPu3PFNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))   
akPu3PFNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
akPu3PFPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))



# secondary vertex b-tag
akPu3PFSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
akPu3PFSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("akPu3PFImpactParameterTagInfos")
akPu3PFSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
akPu3PFSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
akPu3PFSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
akPu3PFSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
akPu3PFCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
akPu3PFCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
akPu3PFCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
akPu3PFCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("akPu3PFSecondaryVertexTagInfos"))

# secondary vertex negative taggers
from RecoBTag.SecondaryVertex.secondaryVertexNegativeTagInfos_cfi import *
from RecoBTag.SecondaryVertex.simpleSecondaryVertexNegativeHighEffBJetTags_cfi import *
from RecoBTag.SecondaryVertex.simpleSecondaryVertexNegativeHighPurBJetTags_cfi import *
from RecoBTag.SecondaryVertex.combinedSecondaryVertexNegativeES_cfi import *
from RecoBTag.SecondaryVertex.combinedSecondaryVertexNegativeBJetTags_cfi import *
from RecoBTag.SecondaryVertex.combinedSecondaryVertexPositiveES_cfi import *
from RecoBTag.SecondaryVertex.combinedSecondaryVertexPositiveBJetTags_cfi import *

akPu3PFSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
akPu3PFSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("akPu3PFImpactParameterTagInfos")
akPu3PFSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
akPu3PFSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexNegativeTagInfos"))
akPu3PFSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
akPu3PFSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexNegativeTagInfos"))
akPu3PFCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
akPu3PFCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("akPu3PFSecondaryVertexNegativeTagInfos"))
akPu3PFCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
akPu3PFCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("akPu3PFSecondaryVertexTagInfos"))

# soft muon b-tag
akPu3PFSoftMuonTagInfos                = softMuonTagInfos.clone()
akPu3PFSoftMuonTagInfos.jets           = cms.InputTag("akPu3PFJets")
akPu3PFSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
akPu3PFSoftMuonBJetTags                = softMuonBJetTags.clone()
akPu3PFSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3PFSoftMuonTagInfos"))
akPu3PFSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
akPu3PFSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSoftMuonTagInfos"))
akPu3PFSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
akPu3PFSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu3PFSoftMuonTagInfos"))

from RecoBTag.SoftLepton.negativeSoftLeptonByPtES_cfi import *
from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
from RecoBTag.SoftLepton.positiveSoftLeptonByPtES_cfi import *
from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

akPu3PFPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
akPu3PFPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3PFSoftMuonTagInfos"))

# soft muon negative taggers
akPu3PFNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
akPu3PFNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3PFSoftMuonTagInfos"))

# ghost tracks
'''
akPu3PFGhostTrackVertexTagInfos                 = ghostTrackVertexTagInfos.clone()
akPu3PFGhostTrackVertexTagInfos.trackIPTagInfos = cms.InputTag("akPu3PFImpactParameterTagInfos")
akPu3PFGhostTrackBJetTags                       = ghostTrackBJetTags.clone()
akPu3PFGhostTrackBJetTags.tagInfos              = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"),
                                                                cms.InputTag("akPu3PFGhostTrackVertexTagInfos"))
'''

# prepare a path running the new modules
akPu3PFJetTracksAssociator = cms.Sequence(akPu3PFJetTracksAssociatorAtVertex)
akPu3PFJetBtaggingIP       = cms.Sequence(akPu3PFImpactParameterTagInfos * (akPu3PFTrackCountingHighEffBJetTags +
                                                                            akPu3PFTrackCountingHighPurBJetTags +
                                                                            akPu3PFJetProbabilityBJetTags +
                                                                            akPu3PFJetBProbabilityBJetTags +
                                                                            akPu3PFPositiveOnlyJetProbabilityJetTags +
                                                                            akPu3PFNegativeOnlyJetProbabilityJetTags +
                                                                            akPu3PFNegativeTrackCountingHighEffJetTags +
                                                                            akPu3PFNegativeTrackCountingHighPur +
                                                                            akPu3PFNegativeOnlyJetBProbabilityJetTags +
                                                                            akPu3PFPositiveOnlyJetBProbabilityJetTags
                                                                                        )
                                                )

akPu3PFJetBtaggingSV = cms.Sequence(akPu3PFImpactParameterTagInfos *
                                    akPu3PFSecondaryVertexTagInfos * (akPu3PFSimpleSecondaryVertexHighEffBJetTags +
                                                                      akPu3PFSimpleSecondaryVertexHighPurBJetTags +
                                                                      akPu3PFCombinedSecondaryVertexBJetTags +
                                                                      akPu3PFCombinedSecondaryVertexMVABJetTags
                                                                      )
                                    #+akPu3PFGhostTrackVertexTagInfos
                                    #*akPu3PFGhostTrackBJetTags
                                    )

akPu3PFJetBtaggingNegSV = cms.Sequence(akPu3PFImpactParameterTagInfos *
                                       akPu3PFSecondaryVertexNegativeTagInfos * (akPu3PFSimpleSecondaryVertexNegativeHighEffBJetTags +
                                                                                 akPu3PFSimpleSecondaryVertexNegativeHighPurBJetTags +
                                                                                 akPu3PFCombinedSecondaryVertexNegativeBJetTags +
                                                                                 akPu3PFCombinedSecondaryVertexPositiveBJetTags 
                                                                                 )
                                       )


akPu3PFJetBtaggingMu = cms.Sequence(akPu3PFSoftMuonTagInfos * (akPu3PFSoftMuonBJetTags +
                                                               akPu3PFSoftMuonByIP3dBJetTags +
                                                               akPu3PFSoftMuonByPtBJetTags +
                                                               akPu3PFNegativeSoftMuonByPtBJetTags +
                                                               akPu3PFPositiveSoftMuonByPtBJetTags
                                                               )
                                          )

akPu3PFJetBtagging = cms.Sequence(akPu3PFJetBtaggingIP 
                                  *akPu3PFJetBtaggingSV 
                                  *akPu3PFJetBtaggingNegSV
                                  *akPu3PFJetBtaggingMu
                                  )

#__________________________________________________________
# ----- flavour bit
akPu3PFPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("akPu3PFJets"),
                                                                                     partons = cms.InputTag("genPartons"),
                                                                                     coneSizeToAssociate = cms.double(0.4))
akPu3PFPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("akPu3PFPatJetPartonAssociation"))

akPu3PFPatJetFlavourId               = cms.Sequence(akPu3PFPatJetPartonAssociation*akPu3PFPatJetFlavourAssociation)
#
#-------
#akPu3PFcorr = patJetCorrFactors.clone(src     = cms.InputTag("akPu3PFJets"),
#                                      levels  = cms.vstring('L2Relative','L3Absolute'),
#                                      payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#                                                      )
akPu3PFmatch   = patJetGenJetMatch.clone(src      = cms.InputTag("akPu3PFJets"),
                                                         matched  = cms.InputTag("ak3clean"))
akPu3PFparton  = patJetPartonMatch.clone(src      = cms.InputTag("akPu3PFJets"))
akPu3PFpatJets = patJets.clone(jetSource            = cms.InputTag("akPu3PFJets"),
                                               genJetMatch          = cms.InputTag("akPu3PFmatch"),
                                               genPartonMatch       = cms.InputTag("akPu3PFparton"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr")),
                                               JetPartonMapSource   = cms.InputTag("akPu3PFPatJetFlavourAssociation"),
                                               trackAssociationSource = cms.InputTag("akPu3PFJetTracksAssociatorAtVertex"),
                                               discriminatorSources = cms.VInputTag(cms.InputTag("akPu3PFSimpleSecondaryVertexHighEffBJetTags"),
                                                                                    cms.InputTag("akPu3PFSimpleSecondaryVertexHighPurBJetTags"),
                                                                                    cms.InputTag("akPu3PFCombinedSecondaryVertexBJetTags"),
                                                                                    cms.InputTag("akPu3PFCombinedSecondaryVertexMVABJetTags"),
                                                                                    cms.InputTag("akPu3PFJetBProbabilityBJetTags"),
                                                                                    cms.InputTag("akPu3PFJetProbabilityBJetTags"),
                                                                                    cms.InputTag("akPu3PFSoftMuonByPtBJetTags"),                
                                                                                    cms.InputTag("akPu3PFSoftMuonByIP3dBJetTags"),
                                                                                    cms.InputTag("akPu3PFTrackCountingHighEffBJetTags"),
                                                                                    cms.InputTag("akPu3PFTrackCountingHighPurBJetTags"),
                                                                                    ),
                                               jetIDMap = cms.InputTag("akPu3PFJetID"),
                                               )


#### B-tagging for this bit:
# b-tagging general configuration
akPu5PFJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
akPu5PFJetTracksAssociatorAtVertex.jets   = cms.InputTag("akPu5PFJets")
akPu5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag
akPu5PFImpactParameterTagInfos               = impactParameterTagInfos.clone()
akPu5PFImpactParameterTagInfos.jetTracks     = cms.InputTag("akPu5PFJetTracksAssociatorAtVertex")
akPu5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu5PFTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
akPu5PFTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
akPu5PFTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
akPu5PFTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
akPu5PFJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()
akPu5PFJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
akPu5PFJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
akPu5PFJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))

#negative impact parameter
#from RecoBTag.ImpactParameter.positiveOnlyJetProbabilityJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeOnlyJetProbabilityJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeTrackCountingHighEffJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeTrackCountingHighPur_cfi import *
#from RecoBTag.ImpactParameter.negativeOnlyJetBProbabilityJetTags_cfi import *

akPu5PFPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()  
akPu5PFNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()    
akPu5PFNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()  
akPu5PFNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()         
akPu5PFNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
akPu5PFPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

akPu5PFPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
akPu5PFNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
akPu5PFNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
akPu5PFNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))   
akPu5PFNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
akPu5PFPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))



# secondary vertex b-tag
akPu5PFSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
akPu5PFSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("akPu5PFImpactParameterTagInfos")
akPu5PFSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
akPu5PFSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
akPu5PFSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
akPu5PFSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
akPu5PFCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
akPu5PFCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
akPu5PFCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
akPu5PFCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("akPu5PFSecondaryVertexTagInfos"))

# secondary vertex negative taggers
#from RecoBTag.SecondaryVertex.secondaryVertexNegativeTagInfos_cfi import *
#from RecoBTag.ImpactParameterLearning.simpleSecondaryVertexNegativeHighEffBJetTags_cfi import *
#from RecoBTag.ImpactParameterLearning.simpleSecondaryVertexNegativeHighPurBJetTags_cfi import *
#from RecoBTag.SecondaryVertex.combinedSecondaryVertexNegativeBJetTags_cfi import *
#from RecoBTag.SecondaryVertex.combinedSecondaryVertexPositiveBJetTags_cfi import *

akPu5PFSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
akPu5PFSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("akPu5PFImpactParameterTagInfos")
akPu5PFSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
akPu5PFSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexNegativeTagInfos"))
akPu5PFSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
akPu5PFSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexNegativeTagInfos"))
akPu5PFCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
akPu5PFCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("akPu5PFSecondaryVertexNegativeTagInfos"))
akPu5PFCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
akPu5PFCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("akPu5PFSecondaryVertexTagInfos"))

# soft muon b-tag
akPu5PFSoftMuonTagInfos                = softMuonTagInfos.clone()
akPu5PFSoftMuonTagInfos.jets           = cms.InputTag("akPu5PFJets")
akPu5PFSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
akPu5PFSoftMuonBJetTags                = softMuonBJetTags.clone()
akPu5PFSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5PFSoftMuonTagInfos"))
akPu5PFSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
akPu5PFSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSoftMuonTagInfos"))
akPu5PFSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
akPu5PFSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu5PFSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

akPu5PFPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
akPu5PFPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5PFSoftMuonTagInfos"))

# soft muon negative taggers
akPu5PFNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
akPu5PFNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5PFSoftMuonTagInfos"))

# ghost tracks
'''
akPu5PFGhostTrackVertexTagInfos                 = ghostTrackVertexTagInfos.clone()
akPu5PFGhostTrackVertexTagInfos.trackIPTagInfos = cms.InputTag("akPu5PFImpactParameterTagInfos")
akPu5PFGhostTrackBJetTags                       = ghostTrackBJetTags.clone()
akPu5PFGhostTrackBJetTags.tagInfos              = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"),
                                                                cms.InputTag("akPu5PFGhostTrackVertexTagInfos"))
'''

# prepare a path running the new modules
akPu5PFJetTracksAssociator = cms.Sequence(akPu5PFJetTracksAssociatorAtVertex)
akPu5PFJetBtaggingIP       = cms.Sequence(akPu5PFImpactParameterTagInfos * (akPu5PFTrackCountingHighEffBJetTags +
                                                                            akPu5PFTrackCountingHighPurBJetTags +
                                                                            akPu5PFJetProbabilityBJetTags +
                                                                            akPu5PFJetBProbabilityBJetTags +
                                                                            akPu5PFPositiveOnlyJetProbabilityJetTags +
                                                                            akPu5PFNegativeOnlyJetProbabilityJetTags +
                                                                            akPu5PFNegativeTrackCountingHighEffJetTags +
                                                                            akPu5PFNegativeTrackCountingHighPur +
                                                                            akPu5PFNegativeOnlyJetBProbabilityJetTags +
                                                                            akPu5PFPositiveOnlyJetBProbabilityJetTags
                                                                                        )
                                                )

akPu5PFJetBtaggingSV = cms.Sequence(akPu5PFImpactParameterTagInfos *
                                    akPu5PFSecondaryVertexTagInfos * (akPu5PFSimpleSecondaryVertexHighEffBJetTags +
                                                                      akPu5PFSimpleSecondaryVertexHighPurBJetTags +
                                                                      akPu5PFCombinedSecondaryVertexBJetTags +
                                                                      akPu5PFCombinedSecondaryVertexMVABJetTags
                                                                      )
                                    #+akPu5PFGhostTrackVertexTagInfos
                                    #*akPu5PFGhostTrackBJetTags
                                    )

akPu5PFJetBtaggingNegSV = cms.Sequence(akPu5PFImpactParameterTagInfos *
                                       akPu5PFSecondaryVertexNegativeTagInfos * (akPu5PFSimpleSecondaryVertexNegativeHighEffBJetTags +
                                                                                 akPu5PFSimpleSecondaryVertexNegativeHighPurBJetTags +
                                                                                 akPu5PFCombinedSecondaryVertexNegativeBJetTags +
                                                                                 akPu5PFCombinedSecondaryVertexPositiveBJetTags 
                                                                                 )
                                       )


akPu5PFJetBtaggingMu = cms.Sequence(akPu5PFSoftMuonTagInfos * (akPu5PFSoftMuonBJetTags +
                                                               akPu5PFSoftMuonByIP3dBJetTags +
                                                               akPu5PFSoftMuonByPtBJetTags +
                                                               akPu5PFNegativeSoftMuonByPtBJetTags +
                                                               akPu5PFPositiveSoftMuonByPtBJetTags
                                                               )
                                          )

akPu5PFJetBtagging = cms.Sequence(akPu5PFJetBtaggingIP 
                                  *akPu5PFJetBtaggingSV 
                                  *akPu5PFJetBtaggingNegSV
                                  *akPu5PFJetBtaggingMu
                                  )

#__________________________________________________________
# ----- flavour bit
akPu5PFPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("akPu5PFJets"),
                                                                                     partons = cms.InputTag("genPartons"),
                                                                                     coneSizeToAssociate = cms.double(0.4))
akPu5PFPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("akPu5PFPatJetPartonAssociation"))

akPu5PFPatJetFlavourId               = cms.Sequence(akPu5PFPatJetPartonAssociation*akPu5PFPatJetFlavourAssociation)
#
#-------
#akPu5PFcorr = patJetCorrFactors.clone(src     = cms.InputTag("akPu5PFJets"),
#                                      levels  = cms.vstring('L2Relative','L3Absolute'),
#                                      payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#                                                      )
akPu5PFmatch   = patJetGenJetMatch.clone(src      = cms.InputTag("akPu5PFJets"),
                                                         matched  = cms.InputTag("ak5clean"))
akPu5PFparton  = patJetPartonMatch.clone(src      = cms.InputTag("akPu5PFJets"))
akPu5PFpatJets = patJets.clone(jetSource            = cms.InputTag("akPu5PFJets"),
                                               genJetMatch          = cms.InputTag("akPu5PFmatch"),
                                               genPartonMatch       = cms.InputTag("akPu5PFparton"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5PFcorr")),
                                               JetPartonMapSource   = cms.InputTag("akPu5PFPatJetFlavourAssociation"),
                                               trackAssociationSource = cms.InputTag("akPu5PFJetTracksAssociatorAtVertex"),
                                               discriminatorSources = cms.VInputTag(cms.InputTag("akPu5PFSimpleSecondaryVertexHighEffBJetTags"),
                                                                                    cms.InputTag("akPu5PFSimpleSecondaryVertexHighPurBJetTags"),
                                                                                    cms.InputTag("akPu5PFCombinedSecondaryVertexBJetTags"),
                                                                                    cms.InputTag("akPu5PFCombinedSecondaryVertexMVABJetTags"),
                                                                                    cms.InputTag("akPu5PFJetBProbabilityBJetTags"),
                                                                                    cms.InputTag("akPu5PFJetProbabilityBJetTags"),
                                                                                    cms.InputTag("akPu5PFSoftMuonByPtBJetTags"),                
                                                                                    cms.InputTag("akPu5PFSoftMuonByIP3dBJetTags"),
                                                                                    cms.InputTag("akPu5PFTrackCountingHighEffBJetTags"),
                                                                                    cms.InputTag("akPu5PFTrackCountingHighPurBJetTags"),
                                                                                    ),
                                               jetIDMap = cms.InputTag("akPu5PFJetID"),
                                               )

  ####################################################################################

#### B-tagging for this bit:
# b-tagging general configuration
ak5PFJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
ak5PFJetTracksAssociatorAtVertex.jets   = cms.InputTag("ak5PFJets")
ak5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag
ak5PFImpactParameterTagInfos               = impactParameterTagInfos.clone()
ak5PFImpactParameterTagInfos.jetTracks     = cms.InputTag("ak5PFJetTracksAssociatorAtVertex")
ak5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak5PFTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
ak5PFTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))
ak5PFTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
ak5PFTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))
ak5PFJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()
ak5PFJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))
ak5PFJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
ak5PFJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))

#negative impact parameter
#from RecoBTag.ImpactParameter.positiveOnlyJetProbabilityJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeOnlyJetProbabilityJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeTrackCountingHighEffJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeTrackCountingHighPur_cfi import *
#from RecoBTag.ImpactParameter.negativeOnlyJetBProbabilityJetTags_cfi import *

ak5PFPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()  
ak5PFNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()    
ak5PFNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()  
ak5PFNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()         
ak5PFNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
ak5PFPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

ak5PFPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))
ak5PFNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))
ak5PFNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))
ak5PFNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))   
ak5PFNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))
ak5PFPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"))



# secondary vertex b-tag
ak5PFSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
ak5PFSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("ak5PFImpactParameterTagInfos")
ak5PFSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
ak5PFSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5PFSecondaryVertexTagInfos"))
ak5PFSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
ak5PFSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5PFSecondaryVertexTagInfos"))
ak5PFCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
ak5PFCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("ak5PFSecondaryVertexTagInfos"))
ak5PFCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
ak5PFCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("ak5PFSecondaryVertexTagInfos"))

# secondary vertex negative taggers
#from RecoBTag.SecondaryVertex.secondaryVertexNegativeTagInfos_cfi import *
#from RecoBTag.ImpactParameterLearning.simpleSecondaryVertexNegativeHighEffBJetTags_cfi import *
#from RecoBTag.ImpactParameterLearning.simpleSecondaryVertexNegativeHighPurBJetTags_cfi import *
#from RecoBTag.SecondaryVertex.combinedSecondaryVertexNegativeBJetTags_cfi import *
#from RecoBTag.SecondaryVertex.combinedSecondaryVertexPositiveBJetTags_cfi import *

ak5PFSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
ak5PFSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("ak5PFImpactParameterTagInfos")
ak5PFSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
ak5PFSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5PFSecondaryVertexNegativeTagInfos"))
ak5PFSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
ak5PFSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5PFSecondaryVertexNegativeTagInfos"))
ak5PFCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
ak5PFCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("ak5PFSecondaryVertexNegativeTagInfos"))
ak5PFCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
ak5PFCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("ak5PFSecondaryVertexTagInfos"))

# soft muon b-tag
ak5PFSoftMuonTagInfos                = softMuonTagInfos.clone()
ak5PFSoftMuonTagInfos.jets           = cms.InputTag("ak5PFJets")
ak5PFSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
ak5PFSoftMuonBJetTags                = softMuonBJetTags.clone()
ak5PFSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5PFSoftMuonTagInfos"))
ak5PFSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
ak5PFSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5PFSoftMuonTagInfos"))
ak5PFSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
ak5PFSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak5PFSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

ak5PFPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
ak5PFPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5PFSoftMuonTagInfos"))

# soft muon negative taggers
ak5PFNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
ak5PFNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5PFSoftMuonTagInfos"))

# ghost tracks
'''
ak5PFGhostTrackVertexTagInfos                 = ghostTrackVertexTagInfos.clone()
ak5PFGhostTrackVertexTagInfos.trackIPTagInfos = cms.InputTag("ak5PFImpactParameterTagInfos")
ak5PFGhostTrackBJetTags                       = ghostTrackBJetTags.clone()
ak5PFGhostTrackBJetTags.tagInfos              = cms.VInputTag(cms.InputTag("ak5PFImpactParameterTagInfos"),
                                                                cms.InputTag("ak5PFGhostTrackVertexTagInfos"))
'''

# prepare a path running the new modules
ak5PFJetTracksAssociator = cms.Sequence(ak5PFJetTracksAssociatorAtVertex)
ak5PFJetBtaggingIP       = cms.Sequence(ak5PFImpactParameterTagInfos * (ak5PFTrackCountingHighEffBJetTags +
                                                                            ak5PFTrackCountingHighPurBJetTags +
                                                                            ak5PFJetProbabilityBJetTags +
                                                                            ak5PFJetBProbabilityBJetTags +
                                                                            ak5PFPositiveOnlyJetProbabilityJetTags +
                                                                            ak5PFNegativeOnlyJetProbabilityJetTags +
                                                                            ak5PFNegativeTrackCountingHighEffJetTags +
                                                                            ak5PFNegativeTrackCountingHighPur +
                                                                            ak5PFNegativeOnlyJetBProbabilityJetTags +
                                                                            ak5PFPositiveOnlyJetBProbabilityJetTags
                                                                                        )
                                                )

ak5PFJetBtaggingSV = cms.Sequence(ak5PFImpactParameterTagInfos *
                                    ak5PFSecondaryVertexTagInfos * (ak5PFSimpleSecondaryVertexHighEffBJetTags +
                                                                      ak5PFSimpleSecondaryVertexHighPurBJetTags +
                                                                      ak5PFCombinedSecondaryVertexBJetTags +
                                                                      ak5PFCombinedSecondaryVertexMVABJetTags
                                                                      )
                                    #+ak5PFGhostTrackVertexTagInfos
                                    #*ak5PFGhostTrackBJetTags
                                    )

ak5PFJetBtaggingNegSV = cms.Sequence(ak5PFImpactParameterTagInfos *
                                       ak5PFSecondaryVertexNegativeTagInfos * (ak5PFSimpleSecondaryVertexNegativeHighEffBJetTags +
                                                                                 ak5PFSimpleSecondaryVertexNegativeHighPurBJetTags +
                                                                                 ak5PFCombinedSecondaryVertexNegativeBJetTags +
                                                                                 ak5PFCombinedSecondaryVertexPositiveBJetTags 
                                                                                 )
                                       )


ak5PFJetBtaggingMu = cms.Sequence(ak5PFSoftMuonTagInfos * (ak5PFSoftMuonBJetTags +
                                                               ak5PFSoftMuonByIP3dBJetTags +
                                                               ak5PFSoftMuonByPtBJetTags +
                                                               ak5PFNegativeSoftMuonByPtBJetTags +
                                                               ak5PFPositiveSoftMuonByPtBJetTags
                                                               )
                                          )

ak5PFJetBtagging = cms.Sequence(ak5PFJetBtaggingIP 
                                  *ak5PFJetBtaggingSV 
                                  *ak5PFJetBtaggingNegSV
                                  *ak5PFJetBtaggingMu
                                  )

#__________________________________________________________
# ----- flavour bit
ak5PFPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("ak5PFJets"),
                                                                                     partons = cms.InputTag("genPartons"),
                                                                                     coneSizeToAssociate = cms.double(0.4))
ak5PFPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("ak5PFPatJetPartonAssociation"))

ak5PFPatJetFlavourId               = cms.Sequence(ak5PFPatJetPartonAssociation*ak5PFPatJetFlavourAssociation)
#
#-------
#ak5PFcorr = patJetCorrFactors.clone(src     = cms.InputTag("ak5PFJets"),
#                                      levels  = cms.vstring('L2Relative','L3Absolute'),
#                                      payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#                                                      )
ak5PFmatch   = patJetGenJetMatch.clone(src      = cms.InputTag("ak5PFJets"),
                                                         matched  = cms.InputTag("ak5clean"))
ak5PFparton  = patJetPartonMatch.clone(src      = cms.InputTag("ak5PFJets"))
ak5PFpatJets = patJets.clone(jetSource            = cms.InputTag("ak5PFJets"),
                                               genJetMatch          = cms.InputTag("ak5PFmatch"),
                                               genPartonMatch       = cms.InputTag("ak5PFparton"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5PFcorr")),
                                               JetPartonMapSource   = cms.InputTag("ak5PFPatJetFlavourAssociation"),
                                               trackAssociationSource = cms.InputTag("ak5PFJetTracksAssociatorAtVertex"),
                                               discriminatorSources = cms.VInputTag(cms.InputTag("ak5PFSimpleSecondaryVertexHighEffBJetTags"),
                                                                                    cms.InputTag("ak5PFSimpleSecondaryVertexHighPurBJetTags"),
                                                                                    cms.InputTag("ak5PFCombinedSecondaryVertexBJetTags"),
                                                                                    cms.InputTag("ak5PFCombinedSecondaryVertexMVABJetTags"),
                                                                                    cms.InputTag("ak5PFJetBProbabilityBJetTags"),
                                                                                    cms.InputTag("ak5PFJetProbabilityBJetTags"),
                                                                                    cms.InputTag("ak5PFSoftMuonByPtBJetTags"),                
                                                                                    cms.InputTag("ak5PFSoftMuonByIP3dBJetTags"),
                                                                                    cms.InputTag("ak5PFTrackCountingHighEffBJetTags"),
                                                                                    cms.InputTag("ak5PFTrackCountingHighPurBJetTags"),
                                                                                    ),
                                               jetIDMap = cms.InputTag("ak5PFJetID"),
                                               )
  
  
  #################################################################################

#### B-tagging for this bit:
# b-tagging general configuration
ak3PFJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
ak3PFJetTracksAssociatorAtVertex.jets   = cms.InputTag("ak3PFJets")
ak3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag
ak3PFImpactParameterTagInfos               = impactParameterTagInfos.clone()
ak3PFImpactParameterTagInfos.jetTracks     = cms.InputTag("ak3PFJetTracksAssociatorAtVertex")
ak3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak3PFTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
ak3PFTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
ak3PFTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
ak3PFTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
ak3PFJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()
ak3PFJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
ak3PFJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
ak3PFJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))

#negative impact parameter
#from RecoBTag.ImpactParameter.positiveOnlyJetProbabilityJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeOnlyJetProbabilityJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeTrackCountingHighEffJetTags_cfi import *
#from RecoBTag.ImpactParameter.negativeTrackCountingHighPur_cfi import *
#from RecoBTag.ImpactParameter.negativeOnlyJetBProbabilityJetTags_cfi import *

ak3PFPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()  
ak3PFNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()    
ak3PFNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()  
ak3PFNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()         
ak3PFNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
ak3PFPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

ak3PFPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
ak3PFNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
ak3PFNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
ak3PFNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))   
ak3PFNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
ak3PFPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))



# secondary vertex b-tag
ak3PFSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
ak3PFSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("ak3PFImpactParameterTagInfos")
ak3PFSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
ak3PFSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexTagInfos"))
ak3PFSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
ak3PFSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexTagInfos"))
ak3PFCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
ak3PFCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("ak3PFSecondaryVertexTagInfos"))
ak3PFCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
ak3PFCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), 
                                                                   cms.InputTag("ak3PFSecondaryVertexTagInfos"))

# secondary vertex negative taggers
#from RecoBTag.SecondaryVertex.secondaryVertexNegativeTagInfos_cfi import *
#from RecoBTag.ImpactParameterLearning.simpleSecondaryVertexNegativeHighEffBJetTags_cfi import *
#from RecoBTag.ImpactParameterLearning.simpleSecondaryVertexNegativeHighPurBJetTags_cfi import *
#from RecoBTag.SecondaryVertex.combinedSecondaryVertexNegativeBJetTags_cfi import *
#from RecoBTag.SecondaryVertex.combinedSecondaryVertexPositiveBJetTags_cfi import *

ak3PFSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
ak3PFSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("ak3PFImpactParameterTagInfos")
ak3PFSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
ak3PFSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexNegativeTagInfos"))
ak3PFSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
ak3PFSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexNegativeTagInfos"))
ak3PFCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
ak3PFCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("ak3PFSecondaryVertexNegativeTagInfos"))
ak3PFCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
ak3PFCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), 
                                                                           cms.InputTag("ak3PFSecondaryVertexTagInfos"))

# soft muon b-tag
ak3PFSoftMuonTagInfos                = softMuonTagInfos.clone()
ak3PFSoftMuonTagInfos.jets           = cms.InputTag("ak3PFJets")
ak3PFSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
ak3PFSoftMuonBJetTags                = softMuonBJetTags.clone()
ak3PFSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3PFSoftMuonTagInfos"))
ak3PFSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
ak3PFSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3PFSoftMuonTagInfos"))
ak3PFSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
ak3PFSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak3PFSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

ak3PFPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
ak3PFPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3PFSoftMuonTagInfos"))

# soft muon negative taggers
ak3PFNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
ak3PFNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3PFSoftMuonTagInfos"))

# ghost tracks
'''
ak3PFGhostTrackVertexTagInfos                 = ghostTrackVertexTagInfos.clone()
ak3PFGhostTrackVertexTagInfos.trackIPTagInfos = cms.InputTag("ak3PFImpactParameterTagInfos")
ak3PFGhostTrackBJetTags                       = ghostTrackBJetTags.clone()
ak3PFGhostTrackBJetTags.tagInfos              = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"),
                                                                cms.InputTag("ak3PFGhostTrackVertexTagInfos"))
'''

# prepare a path running the new modules
ak3PFJetTracksAssociator = cms.Sequence(ak3PFJetTracksAssociatorAtVertex)
ak3PFJetBtaggingIP       = cms.Sequence(ak3PFImpactParameterTagInfos * (ak3PFTrackCountingHighEffBJetTags +
                                                                            ak3PFTrackCountingHighPurBJetTags +
                                                                            ak3PFJetProbabilityBJetTags +
                                                                            ak3PFJetBProbabilityBJetTags +
                                                                            ak3PFPositiveOnlyJetProbabilityJetTags +
                                                                            ak3PFNegativeOnlyJetProbabilityJetTags +
                                                                            ak3PFNegativeTrackCountingHighEffJetTags +
                                                                            ak3PFNegativeTrackCountingHighPur +
                                                                            ak3PFNegativeOnlyJetBProbabilityJetTags +
                                                                            ak3PFPositiveOnlyJetBProbabilityJetTags
                                                                                        )
                                                )

ak3PFJetBtaggingSV = cms.Sequence(ak3PFImpactParameterTagInfos *
                                    ak3PFSecondaryVertexTagInfos * (ak3PFSimpleSecondaryVertexHighEffBJetTags +
                                                                      ak3PFSimpleSecondaryVertexHighPurBJetTags +
                                                                      ak3PFCombinedSecondaryVertexBJetTags +
                                                                      ak3PFCombinedSecondaryVertexMVABJetTags
                                                                      )
                                    #+ak3PFGhostTrackVertexTagInfos
                                    #*ak3PFGhostTrackBJetTags
                                    )

ak3PFJetBtaggingNegSV = cms.Sequence(ak3PFImpactParameterTagInfos *
                                       ak3PFSecondaryVertexNegativeTagInfos * (ak3PFSimpleSecondaryVertexNegativeHighEffBJetTags +
                                                                                 ak3PFSimpleSecondaryVertexNegativeHighPurBJetTags +
                                                                                 ak3PFCombinedSecondaryVertexNegativeBJetTags +
                                                                                 ak3PFCombinedSecondaryVertexPositiveBJetTags 
                                                                                 )
                                       )


ak3PFJetBtaggingMu = cms.Sequence(ak3PFSoftMuonTagInfos * (ak3PFSoftMuonBJetTags +
                                                               ak3PFSoftMuonByIP3dBJetTags +
                                                               ak3PFSoftMuonByPtBJetTags +
                                                               ak3PFNegativeSoftMuonByPtBJetTags +
                                                               ak3PFPositiveSoftMuonByPtBJetTags
                                                               )
                                          )

ak3PFJetBtagging = cms.Sequence(ak3PFJetBtaggingIP 
                                  *ak3PFJetBtaggingSV 
                                  *ak3PFJetBtaggingNegSV
                                  *ak3PFJetBtaggingMu
                                  )

#__________________________________________________________
# ----- flavour bit
ak3PFPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("ak3PFJets"),
                                                                                     partons = cms.InputTag("genPartons"),
                                                                                     coneSizeToAssociate = cms.double(0.4))
ak3PFPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("ak3PFPatJetPartonAssociation"))

ak3PFPatJetFlavourId               = cms.Sequence(ak3PFPatJetPartonAssociation*ak3PFPatJetFlavourAssociation)
#
#-------
#ak3PFcorr = patJetCorrFactors.clone(src     = cms.InputTag("ak3PFJets"),
#                                      levels  = cms.vstring('L2Relative','L3Absolute'),
#                                      payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#                                                      )
ak3PFmatch   = patJetGenJetMatch.clone(src      = cms.InputTag("ak3PFJets"),
                                                         matched  = cms.InputTag("ak3clean"))
ak3PFparton  = patJetPartonMatch.clone(src      = cms.InputTag("ak3PFJets"))
ak3PFpatJets = patJets.clone(jetSource            = cms.InputTag("ak3PFJets"),
                                               genJetMatch          = cms.InputTag("ak3PFmatch"),
                                               genPartonMatch       = cms.InputTag("ak3PFparton"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3PFcorr")),
                                               JetPartonMapSource   = cms.InputTag("ak3PFPatJetFlavourAssociation"),
                                               trackAssociationSource = cms.InputTag("ak3PFJetTracksAssociatorAtVertex"),
                                               discriminatorSources = cms.VInputTag(cms.InputTag("ak3PFSimpleSecondaryVertexHighEffBJetTags"),
                                                                                    cms.InputTag("ak3PFSimpleSecondaryVertexHighPurBJetTags"),
                                                                                    cms.InputTag("ak3PFCombinedSecondaryVertexBJetTags"),
                                                                                    cms.InputTag("ak3PFCombinedSecondaryVertexMVABJetTags"),
                                                                                    cms.InputTag("ak3PFJetBProbabilityBJetTags"),
                                                                                    cms.InputTag("ak3PFJetProbabilityBJetTags"),
                                                                                    cms.InputTag("ak3PFSoftMuonByPtBJetTags"),                
                                                                                    cms.InputTag("ak3PFSoftMuonByIP3dBJetTags"),
                                                                                    cms.InputTag("ak3PFTrackCountingHighEffBJetTags"),
                                                                                    cms.InputTag("ak3PFTrackCountingHighPurBJetTags"),
                                                                                    ),
                                               jetIDMap = cms.InputTag("ak3PFJetID"),
                                               )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
akPu4PFJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
akPu4PFJetTracksAssociatorAtVertex.jets   = cms.InputTag("akPu4PFJets")
akPu4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
akPu4PFImpactParameterTagInfos               = impactParameterTagInfos.clone()
akPu4PFImpactParameterTagInfos.jetTracks     = cms.InputTag("akPu4PFJetTracksAssociatorAtVertex")
akPu4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu4PFTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
akPu4PFTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
akPu4PFTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
akPu4PFJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
akPu4PFJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))

akPu4PFPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
akPu4PFNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
akPu4PFNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
akPu4PFNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
akPu4PFNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
akPu4PFPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

akPu4PFPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
akPu4PFPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))

# secondary vertex b-tag
akPu4PFSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
akPu4PFSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("akPu4PFImpactParameterTagInfos")
akPu4PFSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
akPu4PFSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
akPu4PFSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
akPu4PFSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
akPu4PFCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
akPu4PFCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"),
        cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
akPu4PFCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
akPu4PFCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"),
        cms.InputTag("akPu4PFSecondaryVertexTagInfos"))

akPu4PFSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
akPu4PFSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("akPu4PFImpactParameterTagInfos")
akPu4PFSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
akPu4PFSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexNegativeTagInfos"))
akPu4PFSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
akPu4PFSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexNegativeTagInfos"))
akPu4PFCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
akPu4PFCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"),
        cms.InputTag("akPu4PFSecondaryVertexNegativeTagInfos"))
akPu4PFCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
akPu4PFCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"),
        cms.InputTag("akPu4PFSecondaryVertexTagInfos"))

# soft muon b-tag
akPu4PFSoftMuonTagInfos                = softMuonTagInfos.clone()
akPu4PFSoftMuonTagInfos.jets           = cms.InputTag("akPu4PFJets")
akPu4PFSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
akPu4PFSoftMuonBJetTags                = softMuonBJetTags.clone()
akPu4PFSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4PFSoftMuonTagInfos"))
akPu4PFSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
akPu4PFSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSoftMuonTagInfos"))
akPu4PFSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
akPu4PFSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu4PFSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

akPu4PFPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
akPu4PFPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4PFSoftMuonTagInfos"))

# soft muon negative taggers
akPu4PFNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
akPu4PFNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4PFSoftMuonTagInfos"))

# prepare a path running the new modules
akPu4PFJetTracksAssociator = cms.Sequence(akPu4PFJetTracksAssociatorAtVertex)
akPu4PFJetBtaggingIP       = cms.Sequence(akPu4PFImpactParameterTagInfos * (akPu4PFTrackCountingHighEffBJetTags +
    akPu4PFTrackCountingHighPurBJetTags +
    akPu4PFJetProbabilityBJetTags +
    akPu4PFJetBProbabilityBJetTags +
    akPu4PFPositiveOnlyJetProbabilityJetTags +
    akPu4PFNegativeOnlyJetProbabilityJetTags +
    akPu4PFNegativeTrackCountingHighEffJetTags +
    akPu4PFNegativeTrackCountingHighPur +
    akPu4PFNegativeOnlyJetBProbabilityJetTags +
    akPu4PFPositiveOnlyJetBProbabilityJetTags
    )
    )                          

akPu4PFJetBtaggingSV = cms.Sequence(akPu4PFImpactParameterTagInfos *
        akPu4PFSecondaryVertexTagInfos * (akPu4PFSimpleSecondaryVertexHighEffBJetTags +
            akPu4PFSimpleSecondaryVertexHighPurBJetTags +
            akPu4PFCombinedSecondaryVertexBJetTags +
            akPu4PFCombinedSecondaryVertexMVABJetTags
            )
        #+akPu4PFGhostTrackVertexTagInfos
        #*akPu4PFGhostTrackBJetTags
        )  

akPu4PFJetBtaggingNegSV = cms.Sequence(akPu4PFImpactParameterTagInfos *
        akPu4PFSecondaryVertexNegativeTagInfos * (akPu4PFSimpleSecondaryVertexNegativeHighEffBJetTags +
            akPu4PFSimpleSecondaryVertexNegativeHighPurBJetTags +
            akPu4PFCombinedSecondaryVertexNegativeBJetTags +
            akPu4PFCombinedSecondaryVertexPositiveBJetTags
            )
        )


akPu4PFJetBtaggingMu = cms.Sequence(akPu4PFSoftMuonTagInfos * (akPu4PFSoftMuonBJetTags +
    akPu4PFSoftMuonByIP3dBJetTags +
    akPu4PFSoftMuonByPtBJetTags +
    akPu4PFNegativeSoftMuonByPtBJetTags +
    akPu4PFPositiveSoftMuonByPtBJetTags
    )
    )

akPu4PFJetBtagging = cms.Sequence(akPu4PFJetBtaggingIP
        *akPu4PFJetBtaggingSV
        *akPu4PFJetBtaggingNegSV
        *akPu4PFJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
akPu4PFPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("akPu4PFJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
akPu4PFPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("akPu4PFPatJetPartonAssociation"))

akPu4PFPatJetFlavourId               = cms.Sequence(akPu4PFPatJetPartonAssociation*akPu4PFPatJetFlavourAssociation)
#
#-------
#akPu4PFcorr = patJetCorrFactors.clone(src     = cms.InputTag("akPu4PFJets"),
#                                      levels  = cms.vstring('L2Relative','L3Absolute'),
#                                      payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#                                                      )
akPu4PFmatch   = patJetGenJetMatch.clone(src      = cms.InputTag("akPu4PFJets"),
        matched  = cms.InputTag("ak4clean"))
akPu4PFparton  = patJetPartonMatch.clone(src      = cms.InputTag("akPu4PFJets"))
akPu4PFpatJets = patJets.clone(jetSource            = cms.InputTag("akPu4PFJets"),
        genJetMatch          = cms.InputTag("akPu4PFmatch"),
        genPartonMatch       = cms.InputTag("akPu4PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPu4PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu4PFJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu4PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu4PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu4PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu4PFCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("akPu4PFJetBProbabilityBJetTags"),
            cms.InputTag("akPu4PFJetProbabilityBJetTags"),
            cms.InputTag("akPu4PFSoftMuonByPtBJetTags"),
            cms.InputTag("akPu4PFSoftMuonByIP3dBJetTags"),
            cms.InputTag("akPu4PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu4PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu4PFJetID"),
        )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
ak4PFJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
ak4PFJetTracksAssociatorAtVertex.jets   = cms.InputTag("ak4PFJets")
ak4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
ak4PFImpactParameterTagInfos               = impactParameterTagInfos.clone()
ak4PFImpactParameterTagInfos.jetTracks     = cms.InputTag("ak4PFJetTracksAssociatorAtVertex")
ak4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak4PFTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
ak4PFTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
ak4PFTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
ak4PFJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
ak4PFJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))

ak4PFPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
ak4PFNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
ak4PFNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
ak4PFNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
ak4PFNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
ak4PFPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

ak4PFPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
ak4PFPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))

# secondary vertex b-tag
ak4PFSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
ak4PFSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("ak4PFImpactParameterTagInfos")
ak4PFSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
ak4PFSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexTagInfos"))
ak4PFSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
ak4PFSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexTagInfos"))
ak4PFCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
ak4PFCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"),
        cms.InputTag("ak4PFSecondaryVertexTagInfos"))
ak4PFCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
ak4PFCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"),
        cms.InputTag("ak4PFSecondaryVertexTagInfos"))

ak4PFSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
ak4PFSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("ak4PFImpactParameterTagInfos")
ak4PFSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
ak4PFSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexNegativeTagInfos"))
ak4PFSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
ak4PFSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexNegativeTagInfos"))
ak4PFCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
ak4PFCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"),
        cms.InputTag("ak4PFSecondaryVertexNegativeTagInfos"))
ak4PFCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
ak4PFCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"),
        cms.InputTag("ak4PFSecondaryVertexTagInfos"))

# soft muon b-tag
ak4PFSoftMuonTagInfos                = softMuonTagInfos.clone()
ak4PFSoftMuonTagInfos.jets           = cms.InputTag("ak4PFJets")
ak4PFSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
ak4PFSoftMuonBJetTags                = softMuonBJetTags.clone()
ak4PFSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4PFSoftMuonTagInfos"))
ak4PFSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
ak4PFSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4PFSoftMuonTagInfos"))
ak4PFSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
ak4PFSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak4PFSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

ak4PFPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
ak4PFPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4PFSoftMuonTagInfos"))

# soft muon negative taggers
ak4PFNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
ak4PFNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4PFSoftMuonTagInfos"))

# prepare a path running the new modules
ak4PFJetTracksAssociator = cms.Sequence(ak4PFJetTracksAssociatorAtVertex)
ak4PFJetBtaggingIP       = cms.Sequence(ak4PFImpactParameterTagInfos * (ak4PFTrackCountingHighEffBJetTags +
    ak4PFTrackCountingHighPurBJetTags +
    ak4PFJetProbabilityBJetTags +
    ak4PFJetBProbabilityBJetTags +
    ak4PFPositiveOnlyJetProbabilityJetTags +
    ak4PFNegativeOnlyJetProbabilityJetTags +
    ak4PFNegativeTrackCountingHighEffJetTags +
    ak4PFNegativeTrackCountingHighPur +
    ak4PFNegativeOnlyJetBProbabilityJetTags +
    ak4PFPositiveOnlyJetBProbabilityJetTags
    )
    )                          

ak4PFJetBtaggingSV = cms.Sequence(ak4PFImpactParameterTagInfos *
        ak4PFSecondaryVertexTagInfos * (ak4PFSimpleSecondaryVertexHighEffBJetTags +
            ak4PFSimpleSecondaryVertexHighPurBJetTags +
            ak4PFCombinedSecondaryVertexBJetTags +
            ak4PFCombinedSecondaryVertexMVABJetTags
            )
        #+ak4PFGhostTrackVertexTagInfos
        #*ak4PFGhostTrackBJetTags
        )  

ak4PFJetBtaggingNegSV = cms.Sequence(ak4PFImpactParameterTagInfos *
        ak4PFSecondaryVertexNegativeTagInfos * (ak4PFSimpleSecondaryVertexNegativeHighEffBJetTags +
            ak4PFSimpleSecondaryVertexNegativeHighPurBJetTags +
            ak4PFCombinedSecondaryVertexNegativeBJetTags +
            ak4PFCombinedSecondaryVertexPositiveBJetTags
            )
        )


ak4PFJetBtaggingMu = cms.Sequence(ak4PFSoftMuonTagInfos * (ak4PFSoftMuonBJetTags +
    ak4PFSoftMuonByIP3dBJetTags +
    ak4PFSoftMuonByPtBJetTags +
    ak4PFNegativeSoftMuonByPtBJetTags +
    ak4PFPositiveSoftMuonByPtBJetTags
    )
    )

ak4PFJetBtagging = cms.Sequence(ak4PFJetBtaggingIP
        *ak4PFJetBtaggingSV
        *ak4PFJetBtaggingNegSV
        *ak4PFJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
ak4PFPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("ak4PFJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
ak4PFPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("ak4PFPatJetPartonAssociation"))

ak4PFPatJetFlavourId               = cms.Sequence(ak4PFPatJetPartonAssociation*ak4PFPatJetFlavourAssociation)
#
#-------
#ak4PFcorr = patJetCorrFactors.clone(src     = cms.InputTag("ak4PFJets"),
#        levels  = cms.vstring('L2Relative','L3Absolute'),
#        payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#        )
ak4PFmatch   = patJetGenJetMatch.clone(src      = cms.InputTag("ak4PFJets"),
        matched  = cms.InputTag("ak4clean"))
ak4PFparton  = patJetPartonMatch.clone(src      = cms.InputTag("ak4PFJets"))
ak4PFpatJets = patJets.clone(jetSource            = cms.InputTag("ak4PFJets"),
        genJetMatch          = cms.InputTag("ak4PFmatch"),
        genPartonMatch       = cms.InputTag("ak4PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4PFcorr")),
        JetPartonMapSource   = cms.InputTag("ak4PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("ak4PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("ak4PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("ak4PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("ak4PFCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("ak4PFJetBProbabilityBJetTags"),
            cms.InputTag("ak4PFJetProbabilityBJetTags"),
            cms.InputTag("ak4PFSoftMuonByPtBJetTags"),
            cms.InputTag("ak4PFSoftMuonByIP3dBJetTags"),
            cms.InputTag("ak4PFTrackCountingHighEffBJetTags"),
            cms.InputTag("ak4PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("ak4PFJetID"),
        )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
ak3CaloJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
ak3CaloJetTracksAssociatorAtVertex.jets   = cms.InputTag("ak3CaloJets")
ak3CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
ak3CaloImpactParameterTagInfos               = impactParameterTagInfos.clone()
ak3CaloImpactParameterTagInfos.jetTracks     = cms.InputTag("ak3CaloJetTracksAssociatorAtVertex")
ak3CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak3CaloTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
ak3CaloTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
ak3CaloTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
ak3CaloJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
ak3CaloJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))

ak3CaloPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
ak3CaloNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
ak3CaloNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
ak3CaloNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
ak3CaloNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
ak3CaloPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

ak3CaloPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))
ak3CaloPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"))

# secondary vertex b-tag
ak3CaloSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
ak3CaloSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("ak3CaloImpactParameterTagInfos")
ak3CaloSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
ak3CaloSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3CaloSecondaryVertexTagInfos"))
ak3CaloSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
ak3CaloSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3CaloSecondaryVertexTagInfos"))
ak3CaloCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
ak3CaloCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"),
        cms.InputTag("ak3CaloSecondaryVertexTagInfos"))
ak3CaloCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
ak3CaloCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"),
        cms.InputTag("ak3CaloSecondaryVertexTagInfos"))

ak3CaloSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
ak3CaloSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("ak3CaloImpactParameterTagInfos")
ak3CaloSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
ak3CaloSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3CaloSecondaryVertexNegativeTagInfos"))
ak3CaloSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
ak3CaloSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak3CaloSecondaryVertexNegativeTagInfos"))
ak3CaloCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
ak3CaloCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"),
        cms.InputTag("ak3CaloSecondaryVertexNegativeTagInfos"))
ak3CaloCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
ak3CaloCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak3CaloImpactParameterTagInfos"),
        cms.InputTag("ak3CaloSecondaryVertexTagInfos"))

# soft muon b-tag
ak3CaloSoftMuonTagInfos                = softMuonTagInfos.clone()
ak3CaloSoftMuonTagInfos.jets           = cms.InputTag("ak3CaloJets")
ak3CaloSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
ak3CaloSoftMuonBJetTags                = softMuonBJetTags.clone()
ak3CaloSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3CaloSoftMuonTagInfos"))
ak3CaloSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
ak3CaloSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak3CaloSoftMuonTagInfos"))
ak3CaloSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
ak3CaloSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak3CaloSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

ak3CaloPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
ak3CaloPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3CaloSoftMuonTagInfos"))

# soft muon negative taggers
ak3CaloNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
ak3CaloNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak3CaloSoftMuonTagInfos"))

# prepare a path running the new modules
ak3CaloJetTracksAssociator = cms.Sequence(ak3CaloJetTracksAssociatorAtVertex)
ak3CaloJetBtaggingIP       = cms.Sequence(ak3CaloImpactParameterTagInfos * (ak3CaloTrackCountingHighEffBJetTags +
    ak3CaloTrackCountingHighPurBJetTags +
    ak3CaloJetProbabilityBJetTags +
    ak3CaloJetBProbabilityBJetTags +
    ak3CaloPositiveOnlyJetProbabilityJetTags +
    ak3CaloNegativeOnlyJetProbabilityJetTags +
    ak3CaloNegativeTrackCountingHighEffJetTags +
    ak3CaloNegativeTrackCountingHighPur +
    ak3CaloNegativeOnlyJetBProbabilityJetTags +
    ak3CaloPositiveOnlyJetBProbabilityJetTags
    )
    )                          

ak3CaloJetBtaggingSV = cms.Sequence(ak3CaloImpactParameterTagInfos *
        ak3CaloSecondaryVertexTagInfos * (ak3CaloSimpleSecondaryVertexHighEffBJetTags +
            ak3CaloSimpleSecondaryVertexHighPurBJetTags +
            ak3CaloCombinedSecondaryVertexBJetTags +
            ak3CaloCombinedSecondaryVertexMVABJetTags
            )
        #+ak3CaloGhostTrackVertexTagInfos
        #*ak3CaloGhostTrackBJetTags
        )  

ak3CaloJetBtaggingNegSV = cms.Sequence(ak3CaloImpactParameterTagInfos *
        ak3CaloSecondaryVertexNegativeTagInfos * (ak3CaloSimpleSecondaryVertexNegativeHighEffBJetTags +
            ak3CaloSimpleSecondaryVertexNegativeHighPurBJetTags +
            ak3CaloCombinedSecondaryVertexNegativeBJetTags +
            ak3CaloCombinedSecondaryVertexPositiveBJetTags
            )
        )


ak3CaloJetBtaggingMu = cms.Sequence(ak3CaloSoftMuonTagInfos * (ak3CaloSoftMuonBJetTags +
    ak3CaloSoftMuonByIP3dBJetTags +
    ak3CaloSoftMuonByPtBJetTags +
    ak3CaloNegativeSoftMuonByPtBJetTags +
    ak3CaloPositiveSoftMuonByPtBJetTags
    )
    )

ak3CaloJetBtagging = cms.Sequence(ak3CaloJetBtaggingIP
        *ak3CaloJetBtaggingSV
        *ak3CaloJetBtaggingNegSV
        *ak3CaloJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
ak3CaloPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("ak3CaloJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
ak3CaloPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("ak3CaloPatJetPartonAssociation"))

ak3CaloPatJetFlavourId               = cms.Sequence(ak3CaloPatJetPartonAssociation*ak3CaloPatJetFlavourAssociation)
#
#-------
#ak3Calocorr = patJetCorrFactors.clone(src     = cms.InputTag("ak3CaloJets"),
#        levels  = cms.vstring('L2Relative','L3Absolute'),
#        payload = cms.string('AK3PFTowers_hiGoodTightTracks')
 #       )
ak3Calomatch   = patJetGenJetMatch.clone(src      = cms.InputTag("ak3CaloJets"),
        matched  = cms.InputTag("ak3clean"))
ak3Caloparton  = patJetPartonMatch.clone(src      = cms.InputTag("ak3CaloJets"))
ak3CalopatJets = patJets.clone(jetSource            = cms.InputTag("ak3CaloJets"),
        genJetMatch          = cms.InputTag("ak3Calomatch"),
        genPartonMatch       = cms.InputTag("ak3Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3Calocorr")),
        JetPartonMapSource   = cms.InputTag("ak3CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("ak3CaloJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("ak3CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("ak3CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("ak3CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("ak3CaloCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("ak3CaloJetBProbabilityBJetTags"),
            cms.InputTag("ak3CaloJetProbabilityBJetTags"),
            cms.InputTag("ak3CaloSoftMuonByPtBJetTags"),
            cms.InputTag("ak3CaloSoftMuonByIP3dBJetTags"),
            cms.InputTag("ak3CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("ak3CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("ak3CaloJetID"),
        )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
ak4CaloJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
ak4CaloJetTracksAssociatorAtVertex.jets   = cms.InputTag("ak4CaloJets")
ak4CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
ak4CaloImpactParameterTagInfos               = impactParameterTagInfos.clone()
ak4CaloImpactParameterTagInfos.jetTracks     = cms.InputTag("ak4CaloJetTracksAssociatorAtVertex")
ak4CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak4CaloTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
ak4CaloTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
ak4CaloTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
ak4CaloJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
ak4CaloJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))

ak4CaloPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
ak4CaloNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
ak4CaloNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
ak4CaloNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
ak4CaloNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
ak4CaloPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

ak4CaloPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
ak4CaloPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))

# secondary vertex b-tag
ak4CaloSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
ak4CaloSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("ak4CaloImpactParameterTagInfos")
ak4CaloSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
ak4CaloSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
ak4CaloSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
ak4CaloSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
ak4CaloCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
ak4CaloCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
ak4CaloCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
ak4CaloCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("ak4CaloSecondaryVertexTagInfos"))

ak4CaloSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
ak4CaloSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("ak4CaloImpactParameterTagInfos")
ak4CaloSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
ak4CaloSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexNegativeTagInfos"))
ak4CaloSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
ak4CaloSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexNegativeTagInfos"))
ak4CaloCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
ak4CaloCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"),
                                                                                   cms.InputTag("ak4CaloSecondaryVertexNegativeTagInfos"))
ak4CaloCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
ak4CaloCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"),
                                                                                   cms.InputTag("ak4CaloSecondaryVertexTagInfos"))

# soft muon b-tag
ak4CaloSoftMuonTagInfos                = softMuonTagInfos.clone()
ak4CaloSoftMuonTagInfos.jets           = cms.InputTag("ak4CaloJets")
ak4CaloSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
ak4CaloSoftMuonBJetTags                = softMuonBJetTags.clone()
ak4CaloSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4CaloSoftMuonTagInfos"))
ak4CaloSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
ak4CaloSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSoftMuonTagInfos"))
ak4CaloSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
ak4CaloSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak4CaloSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

ak4CaloPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
ak4CaloPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4CaloSoftMuonTagInfos"))

# soft muon negative taggers
ak4CaloNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
ak4CaloNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak4CaloSoftMuonTagInfos"))

# prepare a path running the new modules
ak4CaloJetTracksAssociator = cms.Sequence(ak4CaloJetTracksAssociatorAtVertex)
ak4CaloJetBtaggingIP       = cms.Sequence(ak4CaloImpactParameterTagInfos * (ak4CaloTrackCountingHighEffBJetTags +
    ak4CaloTrackCountingHighPurBJetTags +
    ak4CaloJetProbabilityBJetTags +
    ak4CaloJetBProbabilityBJetTags +
    ak4CaloPositiveOnlyJetProbabilityJetTags +
    ak4CaloNegativeOnlyJetProbabilityJetTags +
    ak4CaloNegativeTrackCountingHighEffJetTags +
    ak4CaloNegativeTrackCountingHighPur +
    ak4CaloNegativeOnlyJetBProbabilityJetTags +
    ak4CaloPositiveOnlyJetBProbabilityJetTags
    )
    )                          

ak4CaloJetBtaggingSV = cms.Sequence(ak4CaloImpactParameterTagInfos *
        ak4CaloSecondaryVertexTagInfos * (ak4CaloSimpleSecondaryVertexHighEffBJetTags +
            ak4CaloSimpleSecondaryVertexHighPurBJetTags +
            ak4CaloCombinedSecondaryVertexBJetTags +
            ak4CaloCombinedSecondaryVertexMVABJetTags
            )
        #+ak4CaloGhostTrackVertexTagInfos
        #*ak4CaloGhostTrackBJetTags
        )  

ak4CaloJetBtaggingNegSV = cms.Sequence(ak4CaloImpactParameterTagInfos *
        ak4CaloSecondaryVertexNegativeTagInfos * (ak4CaloSimpleSecondaryVertexNegativeHighEffBJetTags +
            ak4CaloSimpleSecondaryVertexNegativeHighPurBJetTags +
            ak4CaloCombinedSecondaryVertexNegativeBJetTags +
            ak4CaloCombinedSecondaryVertexPositiveBJetTags
            )
        )


ak4CaloJetBtaggingMu = cms.Sequence(ak4CaloSoftMuonTagInfos * (ak4CaloSoftMuonBJetTags +
    ak4CaloSoftMuonByIP3dBJetTags +
    ak4CaloSoftMuonByPtBJetTags +
    ak4CaloNegativeSoftMuonByPtBJetTags +
    ak4CaloPositiveSoftMuonByPtBJetTags
    )
    )

ak4CaloJetBtagging = cms.Sequence(ak4CaloJetBtaggingIP
        *ak4CaloJetBtaggingSV
        *ak4CaloJetBtaggingNegSV
        *ak4CaloJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
ak4CaloPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("ak4CaloJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
ak4CaloPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("ak4CaloPatJetPartonAssociation"))

ak4CaloPatJetFlavourId               = cms.Sequence(ak4CaloPatJetPartonAssociation*ak4CaloPatJetFlavourAssociation)
#
#-------
#ak4Calocorr = patJetCorrFactors.clone(src     = cms.InputTag("ak4CaloJets"),
#        levels  = cms.vstring('L2Relative','L3Absolute'),
#        payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#        )
ak4Calomatch   = patJetGenJetMatch.clone(src      = cms.InputTag("ak4CaloJets"),
        matched  = cms.InputTag("ak4clean"))
ak4Caloparton  = patJetPartonMatch.clone(src      = cms.InputTag("ak4CaloJets"))
ak4CalopatJets = patJets.clone(jetSource            = cms.InputTag("ak4CaloJets"),
        genJetMatch          = cms.InputTag("ak4Calomatch"),
        genPartonMatch       = cms.InputTag("ak4Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4Calocorr")),
        JetPartonMapSource   = cms.InputTag("ak4CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("ak4CaloJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("ak4CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("ak4CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("ak4CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("ak4CaloCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("ak4CaloJetBProbabilityBJetTags"),
            cms.InputTag("ak4CaloJetProbabilityBJetTags"),
            cms.InputTag("ak4CaloSoftMuonByPtBJetTags"),
            cms.InputTag("ak4CaloSoftMuonByIP3dBJetTags"),
            cms.InputTag("ak4CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("ak4CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("ak4CaloJetID"),
        )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
ak5CaloJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
ak5CaloJetTracksAssociatorAtVertex.jets   = cms.InputTag("ak5CaloJets")
ak5CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
ak5CaloImpactParameterTagInfos               = impactParameterTagInfos.clone()
ak5CaloImpactParameterTagInfos.jetTracks     = cms.InputTag("ak5CaloJetTracksAssociatorAtVertex")
ak5CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak5CaloTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
ak5CaloTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
ak5CaloTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
ak5CaloJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
ak5CaloJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))

ak5CaloPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
ak5CaloNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
ak5CaloNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
ak5CaloNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
ak5CaloNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
ak5CaloPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

ak5CaloPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))
ak5CaloPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"))

# secondary vertex b-tag
ak5CaloSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
ak5CaloSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("ak5CaloImpactParameterTagInfos")
ak5CaloSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
ak5CaloSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5CaloSecondaryVertexTagInfos"))
ak5CaloSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
ak5CaloSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5CaloSecondaryVertexTagInfos"))
ak5CaloCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
ak5CaloCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("ak5CaloSecondaryVertexTagInfos"))
ak5CaloCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
ak5CaloCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("ak5CaloSecondaryVertexTagInfos"))

ak5CaloSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
ak5CaloSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("ak5CaloImpactParameterTagInfos")
ak5CaloSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
ak5CaloSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5CaloSecondaryVertexNegativeTagInfos"))
ak5CaloSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
ak5CaloSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("ak5CaloSecondaryVertexNegativeTagInfos"))
ak5CaloCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
ak5CaloCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"),
        cms.InputTag("ak5CaloSecondaryVertexNegativeTagInfos"))
ak5CaloCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
ak5CaloCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("ak5CaloImpactParameterTagInfos"),
        cms.InputTag("ak5CaloSecondaryVertexTagInfos"))

# soft muon b-tag
ak5CaloSoftMuonTagInfos                = softMuonTagInfos.clone()
ak5CaloSoftMuonTagInfos.jets           = cms.InputTag("ak5CaloJets")
ak5CaloSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
ak5CaloSoftMuonBJetTags                = softMuonBJetTags.clone()
ak5CaloSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5CaloSoftMuonTagInfos"))
ak5CaloSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
ak5CaloSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("ak5CaloSoftMuonTagInfos"))
ak5CaloSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
ak5CaloSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("ak5CaloSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

ak5CaloPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
ak5CaloPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5CaloSoftMuonTagInfos"))

# soft muon negative taggers
ak5CaloNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
ak5CaloNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("ak5CaloSoftMuonTagInfos"))

# prepare a path running the new modules
ak5CaloJetTracksAssociator = cms.Sequence(ak5CaloJetTracksAssociatorAtVertex)
ak5CaloJetBtaggingIP       = cms.Sequence(ak5CaloImpactParameterTagInfos * (ak5CaloTrackCountingHighEffBJetTags +
    ak5CaloTrackCountingHighPurBJetTags +
    ak5CaloJetProbabilityBJetTags +
    ak5CaloJetBProbabilityBJetTags +
    ak5CaloPositiveOnlyJetProbabilityJetTags +
    ak5CaloNegativeOnlyJetProbabilityJetTags +
    ak5CaloNegativeTrackCountingHighEffJetTags +
    ak5CaloNegativeTrackCountingHighPur +
    ak5CaloNegativeOnlyJetBProbabilityJetTags +
    ak5CaloPositiveOnlyJetBProbabilityJetTags
    )
    )                          

ak5CaloJetBtaggingSV = cms.Sequence(ak5CaloImpactParameterTagInfos *
        ak5CaloSecondaryVertexTagInfos * (ak5CaloSimpleSecondaryVertexHighEffBJetTags +
            ak5CaloSimpleSecondaryVertexHighPurBJetTags +
            ak5CaloCombinedSecondaryVertexBJetTags +
            ak5CaloCombinedSecondaryVertexMVABJetTags
            )
        #+ak5CaloGhostTrackVertexTagInfos
        #*ak5CaloGhostTrackBJetTags
        )  

ak5CaloJetBtaggingNegSV = cms.Sequence(ak5CaloImpactParameterTagInfos *
        ak5CaloSecondaryVertexNegativeTagInfos * (ak5CaloSimpleSecondaryVertexNegativeHighEffBJetTags +
            ak5CaloSimpleSecondaryVertexNegativeHighPurBJetTags +
            ak5CaloCombinedSecondaryVertexNegativeBJetTags +
            ak5CaloCombinedSecondaryVertexPositiveBJetTags
            )
        )


ak5CaloJetBtaggingMu = cms.Sequence(ak5CaloSoftMuonTagInfos * (ak5CaloSoftMuonBJetTags +
    ak5CaloSoftMuonByIP3dBJetTags +
    ak5CaloSoftMuonByPtBJetTags +
    ak5CaloNegativeSoftMuonByPtBJetTags +
    ak5CaloPositiveSoftMuonByPtBJetTags
    )
    )

ak5CaloJetBtagging = cms.Sequence(ak5CaloJetBtaggingIP
        *ak5CaloJetBtaggingSV
        *ak5CaloJetBtaggingNegSV
        *ak5CaloJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
ak5CaloPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("ak5CaloJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
ak5CaloPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("ak5CaloPatJetPartonAssociation"))

ak5CaloPatJetFlavourId               = cms.Sequence(ak5CaloPatJetPartonAssociation*ak5CaloPatJetFlavourAssociation)
#
#-------
#ak5Calocorr = patJetCorrFactors.clone(src     = cms.InputTag("ak5CaloJets"),
#        levels  = cms.vstring('L2Relative','L3Absolute'),
#        payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#        )
ak5Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3HiGenJets'))
ak5Calomatch   = patJetGenJetMatch.clone(src      = cms.InputTag("ak5CaloJets"),
        matched  = cms.InputTag("ak5clean"))
ak5Caloparton  = patJetPartonMatch.clone(src      = cms.InputTag("ak5CaloJets"))
ak5CalopatJets = patJets.clone(jetSource            = cms.InputTag("ak5CaloJets"),
        genJetMatch          = cms.InputTag("ak5Calomatch"),
        genPartonMatch       = cms.InputTag("ak5Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5Calocorr")),
        JetPartonMapSource   = cms.InputTag("ak5CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("ak5CaloJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("ak5CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("ak5CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("ak5CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("ak5CaloCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("ak5CaloJetBProbabilityBJetTags"),
            cms.InputTag("ak5CaloJetProbabilityBJetTags"),
            cms.InputTag("ak5CaloSoftMuonByPtBJetTags"),
            cms.InputTag("ak5CaloSoftMuonByIP3dBJetTags"),
            cms.InputTag("ak5CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("ak5CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("ak5CaloJetID"),
        )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
akPu5CaloJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
akPu5CaloJetTracksAssociatorAtVertex.jets   = cms.InputTag("akPu5CaloJets")
akPu5CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
akPu5CaloImpactParameterTagInfos               = impactParameterTagInfos.clone()
akPu5CaloImpactParameterTagInfos.jetTracks     = cms.InputTag("akPu5CaloJetTracksAssociatorAtVertex")
akPu5CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu5CaloTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
akPu5CaloTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
akPu5CaloTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
akPu5CaloJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
akPu5CaloJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))

akPu5CaloPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
akPu5CaloNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
akPu5CaloNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
akPu5CaloNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
akPu5CaloNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
akPu5CaloPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

akPu5CaloPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
akPu5CaloPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))

# secondary vertex b-tag
akPu5CaloSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
akPu5CaloSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("akPu5CaloImpactParameterTagInfos")
akPu5CaloSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
akPu5CaloSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
akPu5CaloSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
akPu5CaloSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
akPu5CaloCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
akPu5CaloCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
akPu5CaloCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
akPu5CaloCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))

akPu5CaloSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
akPu5CaloSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("akPu5CaloImpactParameterTagInfos")
akPu5CaloSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
akPu5CaloSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexNegativeTagInfos"))
akPu5CaloSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
akPu5CaloSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexNegativeTagInfos"))
akPu5CaloCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
akPu5CaloCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"),
                                                                                   cms.InputTag("akPu5CaloSecondaryVertexNegativeTagInfos"))
akPu5CaloCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
akPu5CaloCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"),
                                                                                   cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))

# soft muon b-tag
akPu5CaloSoftMuonTagInfos                = softMuonTagInfos.clone()
akPu5CaloSoftMuonTagInfos.jets           = cms.InputTag("akPu5CaloJets")
akPu5CaloSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
akPu5CaloSoftMuonBJetTags                = softMuonBJetTags.clone()
akPu5CaloSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5CaloSoftMuonTagInfos"))
akPu5CaloSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
akPu5CaloSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSoftMuonTagInfos"))
akPu5CaloSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
akPu5CaloSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu5CaloSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

akPu5CaloPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
akPu5CaloPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5CaloSoftMuonTagInfos"))

# soft muon negative taggers
akPu5CaloNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
akPu5CaloNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu5CaloSoftMuonTagInfos"))

# prepare a path running the new modules
akPu5CaloJetTracksAssociator = cms.Sequence(akPu5CaloJetTracksAssociatorAtVertex)
akPu5CaloJetBtaggingIP       = cms.Sequence(akPu5CaloImpactParameterTagInfos * (akPu5CaloTrackCountingHighEffBJetTags +
    akPu5CaloTrackCountingHighPurBJetTags +
    akPu5CaloJetProbabilityBJetTags +
    akPu5CaloJetBProbabilityBJetTags +
    akPu5CaloPositiveOnlyJetProbabilityJetTags +
    akPu5CaloNegativeOnlyJetProbabilityJetTags +
    akPu5CaloNegativeTrackCountingHighEffJetTags +
    akPu5CaloNegativeTrackCountingHighPur +
    akPu5CaloNegativeOnlyJetBProbabilityJetTags +
    akPu5CaloPositiveOnlyJetBProbabilityJetTags
    )
    )                          

akPu5CaloJetBtaggingSV = cms.Sequence(akPu5CaloImpactParameterTagInfos *
        akPu5CaloSecondaryVertexTagInfos * (akPu5CaloSimpleSecondaryVertexHighEffBJetTags +
            akPu5CaloSimpleSecondaryVertexHighPurBJetTags +
            akPu5CaloCombinedSecondaryVertexBJetTags +
            akPu5CaloCombinedSecondaryVertexMVABJetTags
            )
        #+akPu5CaloGhostTrackVertexTagInfos
        #*akPu5CaloGhostTrackBJetTags
        )  

akPu5CaloJetBtaggingNegSV = cms.Sequence(akPu5CaloImpactParameterTagInfos *
        akPu5CaloSecondaryVertexNegativeTagInfos * (akPu5CaloSimpleSecondaryVertexNegativeHighEffBJetTags +
            akPu5CaloSimpleSecondaryVertexNegativeHighPurBJetTags +
            akPu5CaloCombinedSecondaryVertexNegativeBJetTags +
            akPu5CaloCombinedSecondaryVertexPositiveBJetTags
            )
        )


akPu5CaloJetBtaggingMu = cms.Sequence(akPu5CaloSoftMuonTagInfos * (akPu5CaloSoftMuonBJetTags +
    akPu5CaloSoftMuonByIP3dBJetTags +
    akPu5CaloSoftMuonByPtBJetTags +
    akPu5CaloNegativeSoftMuonByPtBJetTags +
    akPu5CaloPositiveSoftMuonByPtBJetTags
    )
    )

akPu5CaloJetBtagging = cms.Sequence(akPu5CaloJetBtaggingIP
        *akPu5CaloJetBtaggingSV
        *akPu5CaloJetBtaggingNegSV
        *akPu5CaloJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
akPu5CaloPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("akPu5CaloJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
akPu5CaloPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("akPu5CaloPatJetPartonAssociation"))

akPu5CaloPatJetFlavourId               = cms.Sequence(akPu5CaloPatJetPartonAssociation*akPu5CaloPatJetFlavourAssociation)
#
#-------
#akPu5Calocorr = patJetCorrFactors.clone(src     = cms.InputTag("akPu5CaloJets"),
#        levels  = cms.vstring('L2Relative','L3Absolute'),
#        payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#        )
akPu5Calomatch   = patJetGenJetMatch.clone(src      = cms.InputTag("akPu5CaloJets"),
        matched  = cms.InputTag("ak5clean"))
akPu5Caloparton  = patJetPartonMatch.clone(src      = cms.InputTag("akPu5CaloJets"))
akPu5CalopatJets = patJets.clone(jetSource            = cms.InputTag("akPu5CaloJets"),
        genJetMatch          = cms.InputTag("akPu5Calomatch"),
        genPartonMatch       = cms.InputTag("akPu5Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPu5CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu5CaloJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu5CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu5CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu5CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu5CaloCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("akPu5CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPu5CaloJetProbabilityBJetTags"),
            cms.InputTag("akPu5CaloSoftMuonByPtBJetTags"),
            cms.InputTag("akPu5CaloSoftMuonByIP3dBJetTags"),
            cms.InputTag("akPu5CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu5CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu5CaloJetID"),
        )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
akPu4CaloJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
akPu4CaloJetTracksAssociatorAtVertex.jets   = cms.InputTag("akPu4CaloJets")
akPu4CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
akPu4CaloImpactParameterTagInfos               = impactParameterTagInfos.clone()
akPu4CaloImpactParameterTagInfos.jetTracks     = cms.InputTag("akPu4CaloJetTracksAssociatorAtVertex")
akPu4CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu4CaloTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
akPu4CaloTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
akPu4CaloTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
akPu4CaloJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
akPu4CaloJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))

akPu4CaloPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
akPu4CaloNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
akPu4CaloNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
akPu4CaloNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
akPu4CaloNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
akPu4CaloPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

akPu4CaloPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
akPu4CaloPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))

# secondary vertex b-tag
akPu4CaloSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
akPu4CaloSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("akPu4CaloImpactParameterTagInfos")
akPu4CaloSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
akPu4CaloSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
akPu4CaloSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
akPu4CaloSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
akPu4CaloCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
akPu4CaloCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
akPu4CaloCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
akPu4CaloCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))

akPu4CaloSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
akPu4CaloSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("akPu4CaloImpactParameterTagInfos")
akPu4CaloSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
akPu4CaloSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexNegativeTagInfos"))
akPu4CaloSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
akPu4CaloSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexNegativeTagInfos"))
akPu4CaloCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
akPu4CaloCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"),
        cms.InputTag("akPu4CaloSecondaryVertexNegativeTagInfos"))
akPu4CaloCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
akPu4CaloCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"),
        cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))

# soft muon b-tag
akPu4CaloSoftMuonTagInfos                = softMuonTagInfos.clone()
akPu4CaloSoftMuonTagInfos.jets           = cms.InputTag("akPu4CaloJets")
akPu4CaloSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
akPu4CaloSoftMuonBJetTags                = softMuonBJetTags.clone()
akPu4CaloSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4CaloSoftMuonTagInfos"))
akPu4CaloSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
akPu4CaloSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSoftMuonTagInfos"))
akPu4CaloSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
akPu4CaloSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu4CaloSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

akPu4CaloPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
akPu4CaloPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4CaloSoftMuonTagInfos"))

# soft muon negative taggers
akPu4CaloNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
akPu4CaloNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu4CaloSoftMuonTagInfos"))

# prepare a path running the new modules
akPu4CaloJetTracksAssociator = cms.Sequence(akPu4CaloJetTracksAssociatorAtVertex)
akPu4CaloJetBtaggingIP       = cms.Sequence(akPu4CaloImpactParameterTagInfos * (akPu4CaloTrackCountingHighEffBJetTags +
    akPu4CaloTrackCountingHighPurBJetTags +
    akPu4CaloJetProbabilityBJetTags +
    akPu4CaloJetBProbabilityBJetTags +
    akPu4CaloPositiveOnlyJetProbabilityJetTags +
    akPu4CaloNegativeOnlyJetProbabilityJetTags +
    akPu4CaloNegativeTrackCountingHighEffJetTags +
    akPu4CaloNegativeTrackCountingHighPur +
    akPu4CaloNegativeOnlyJetBProbabilityJetTags +
    akPu4CaloPositiveOnlyJetBProbabilityJetTags
    )
    )                          

akPu4CaloJetBtaggingSV = cms.Sequence(akPu4CaloImpactParameterTagInfos *
        akPu4CaloSecondaryVertexTagInfos * (akPu4CaloSimpleSecondaryVertexHighEffBJetTags +
            akPu4CaloSimpleSecondaryVertexHighPurBJetTags +
            akPu4CaloCombinedSecondaryVertexBJetTags +
            akPu4CaloCombinedSecondaryVertexMVABJetTags
            )
        #+akPu4CaloGhostTrackVertexTagInfos
        #*akPu4CaloGhostTrackBJetTags
        )  

akPu4CaloJetBtaggingNegSV = cms.Sequence(akPu4CaloImpactParameterTagInfos *
        akPu4CaloSecondaryVertexNegativeTagInfos * (akPu4CaloSimpleSecondaryVertexNegativeHighEffBJetTags +
            akPu4CaloSimpleSecondaryVertexNegativeHighPurBJetTags +
            akPu4CaloCombinedSecondaryVertexNegativeBJetTags +
            akPu4CaloCombinedSecondaryVertexPositiveBJetTags
            )
        )


akPu4CaloJetBtaggingMu = cms.Sequence(akPu4CaloSoftMuonTagInfos * (akPu4CaloSoftMuonBJetTags +
    akPu4CaloSoftMuonByIP3dBJetTags +
    akPu4CaloSoftMuonByPtBJetTags +
    akPu4CaloNegativeSoftMuonByPtBJetTags +
    akPu4CaloPositiveSoftMuonByPtBJetTags
    )
    )

akPu4CaloJetBtagging = cms.Sequence(akPu4CaloJetBtaggingIP
        *akPu4CaloJetBtaggingSV
        *akPu4CaloJetBtaggingNegSV
        *akPu4CaloJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
akPu4CaloPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("akPu4CaloJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
akPu4CaloPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("akPu4CaloPatJetPartonAssociation"))

akPu4CaloPatJetFlavourId               = cms.Sequence(akPu4CaloPatJetPartonAssociation*akPu4CaloPatJetFlavourAssociation)
#
#-------
#akPu4Calocorr = patJetCorrFactors.clone(src     = cms.InputTag("akPu4CaloJets"),
#        levels  = cms.vstring('L2Relative','L3Absolute'),
#        payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#        )
akPu4Calomatch   = patJetGenJetMatch.clone(src      = cms.InputTag("akPu4CaloJets"),
        matched  = cms.InputTag("ak4clean"))
akPu4Caloparton  = patJetPartonMatch.clone(src      = cms.InputTag("akPu4CaloJets"))
akPu4CalopatJets = patJets.clone(jetSource            = cms.InputTag("akPu4CaloJets"),
        genJetMatch          = cms.InputTag("akPu4Calomatch"),
        genPartonMatch       = cms.InputTag("akPu4Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPu4CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu4CaloJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu4CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu4CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu4CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu4CaloCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("akPu4CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPu4CaloJetProbabilityBJetTags"),
            cms.InputTag("akPu4CaloSoftMuonByPtBJetTags"),
            cms.InputTag("akPu4CaloSoftMuonByIP3dBJetTags"),
            cms.InputTag("akPu4CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu4CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu4CaloJetID"),
        )

#### B-tagging for this bit:                                   
# b-tagging general configuration                              
akPu3CaloJetTracksAssociatorAtVertex        = ak5JetTracksAssociatorAtVertex.clone()
akPu3CaloJetTracksAssociatorAtVertex.jets   = cms.InputTag("akPu3CaloJets")
akPu3CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("generalTracks")
# impact parameter b-tag          
akPu3CaloImpactParameterTagInfos               = impactParameterTagInfos.clone()
akPu3CaloImpactParameterTagInfos.jetTracks     = cms.InputTag("akPu3CaloJetTracksAssociatorAtVertex")
akPu3CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu3CaloTrackCountingHighEffBJetTags          = trackCountingHighEffBJetTags.clone()
akPu3CaloTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloTrackCountingHighPurBJetTags          = trackCountingHighPurBJetTags.clone()
akPu3CaloTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloJetProbabilityBJetTags                = jetProbabilityBJetTags.clone()        
akPu3CaloJetProbabilityBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloJetBProbabilityBJetTags               = jetBProbabilityBJetTags.clone()
akPu3CaloJetBProbabilityBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))

akPu3CaloPositiveOnlyJetProbabilityJetTags     =       positiveOnlyJetProbabilityJetTags.clone()
akPu3CaloNegativeOnlyJetProbabilityJetTags     =       negativeOnlyJetProbabilityJetTags.clone()   
akPu3CaloNegativeTrackCountingHighEffJetTags   =       negativeTrackCountingHighEffJetTags.clone()
akPu3CaloNegativeTrackCountingHighPur          =       negativeTrackCountingHighPur.clone()
akPu3CaloNegativeOnlyJetBProbabilityJetTags    =       negativeOnlyJetBProbabilityJetTags.clone()
akPu3CaloPositiveOnlyJetBProbabilityJetTags    =       positiveOnlyJetBProbabilityJetTags.clone()

akPu3CaloPositiveOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloNegativeOnlyJetProbabilityJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloNegativeTrackCountingHighEffJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloNegativeTrackCountingHighPur.tagInfos        = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloNegativeOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
akPu3CaloPositiveOnlyJetBProbabilityJetTags.tagInfos  = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))

# secondary vertex b-tag
akPu3CaloSecondaryVertexTagInfos                     = secondaryVertexTagInfos.clone()
akPu3CaloSecondaryVertexTagInfos.trackIPTagInfos     = cms.InputTag("akPu3CaloImpactParameterTagInfos")
akPu3CaloSimpleSecondaryVertexHighEffBJetTags               = simpleSecondaryVertexHighEffBJetTags.clone()
akPu3CaloSimpleSecondaryVertexHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
akPu3CaloSimpleSecondaryVertexHighPurBJetTags               = simpleSecondaryVertexHighPurBJetTags.clone()
akPu3CaloSimpleSecondaryVertexHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
akPu3CaloCombinedSecondaryVertexBJetTags             = combinedSecondaryVertexBJetTags.clone()
akPu3CaloCombinedSecondaryVertexBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
akPu3CaloCombinedSecondaryVertexMVABJetTags          = combinedSecondaryVertexMVABJetTags.clone()
akPu3CaloCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"),
                                                                           cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))

akPu3CaloSecondaryVertexNegativeTagInfos                     = secondaryVertexNegativeTagInfos.clone()
akPu3CaloSecondaryVertexNegativeTagInfos.trackIPTagInfos     = cms.InputTag("akPu3CaloImpactParameterTagInfos")
akPu3CaloSimpleSecondaryVertexNegativeHighEffBJetTags               = simpleSecondaryVertexNegativeHighEffBJetTags.clone()
akPu3CaloSimpleSecondaryVertexNegativeHighEffBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexNegativeTagInfos"))
akPu3CaloSimpleSecondaryVertexNegativeHighPurBJetTags               = simpleSecondaryVertexNegativeHighPurBJetTags.clone()
akPu3CaloSimpleSecondaryVertexNegativeHighPurBJetTags.tagInfos      = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexNegativeTagInfos"))
akPu3CaloCombinedSecondaryVertexNegativeBJetTags                    = combinedSecondaryVertexNegativeBJetTags.clone()
akPu3CaloCombinedSecondaryVertexNegativeBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"),
        cms.InputTag("akPu3CaloSecondaryVertexNegativeTagInfos"))
akPu3CaloCombinedSecondaryVertexPositiveBJetTags                    = combinedSecondaryVertexPositiveBJetTags.clone()
akPu3CaloCombinedSecondaryVertexPositiveBJetTags.tagInfos    = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"),
        cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))

# soft muon b-tag
akPu3CaloSoftMuonTagInfos                = softMuonTagInfos.clone()
akPu3CaloSoftMuonTagInfos.jets           = cms.InputTag("akPu3CaloJets")
akPu3CaloSoftMuonTagInfos.primaryVertex  = cms.InputTag("offlinePrimaryVertices")
akPu3CaloSoftMuonBJetTags                = softMuonBJetTags.clone()
akPu3CaloSoftMuonBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3CaloSoftMuonTagInfos"))
akPu3CaloSoftMuonByIP3dBJetTags          = softMuonByIP3dBJetTags.clone()
akPu3CaloSoftMuonByIP3dBJetTags.tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSoftMuonTagInfos"))
akPu3CaloSoftMuonByPtBJetTags            = softMuonByPtBJetTags.clone()
akPu3CaloSoftMuonByPtBJetTags.tagInfos   = cms.VInputTag(cms.InputTag("akPu3CaloSoftMuonTagInfos"))

#from RecoBTag.SoftLepton.negativeSoftMuonByPtBJetTags_cfi import *
#from RecoBTag.SoftLepton.positiveSoftMuonByPtBJetTags_cfi import *

akPu3CaloPositiveSoftMuonByPtBJetTags                = positiveSoftLeptonByPtBJetTags.clone()
akPu3CaloPositiveSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3CaloSoftMuonTagInfos"))

# soft muon negative taggers
akPu3CaloNegativeSoftMuonByPtBJetTags                = negativeSoftLeptonByPtBJetTags.clone()
akPu3CaloNegativeSoftMuonByPtBJetTags.tagInfos       = cms.VInputTag(cms.InputTag("akPu3CaloSoftMuonTagInfos"))

# prepare a path running the new modules
akPu3CaloJetTracksAssociator = cms.Sequence(akPu3CaloJetTracksAssociatorAtVertex)
akPu3CaloJetBtaggingIP       = cms.Sequence(akPu3CaloImpactParameterTagInfos * (akPu3CaloTrackCountingHighEffBJetTags +
    akPu3CaloTrackCountingHighPurBJetTags +
    akPu3CaloJetProbabilityBJetTags +
    akPu3CaloJetBProbabilityBJetTags +
    akPu3CaloPositiveOnlyJetProbabilityJetTags +
    akPu3CaloNegativeOnlyJetProbabilityJetTags +
    akPu3CaloNegativeTrackCountingHighEffJetTags +
    akPu3CaloNegativeTrackCountingHighPur +
    akPu3CaloNegativeOnlyJetBProbabilityJetTags +
    akPu3CaloPositiveOnlyJetBProbabilityJetTags
    )
    )                          

akPu3CaloJetBtaggingSV = cms.Sequence(akPu3CaloImpactParameterTagInfos *
        akPu3CaloSecondaryVertexTagInfos * (akPu3CaloSimpleSecondaryVertexHighEffBJetTags +
            akPu3CaloSimpleSecondaryVertexHighPurBJetTags +
            akPu3CaloCombinedSecondaryVertexBJetTags +
            akPu3CaloCombinedSecondaryVertexMVABJetTags
            )
        #+akPu3CaloGhostTrackVertexTagInfos
        #*akPu3CaloGhostTrackBJetTags
        )  

akPu3CaloJetBtaggingNegSV = cms.Sequence(akPu3CaloImpactParameterTagInfos *
        akPu3CaloSecondaryVertexNegativeTagInfos * (akPu3CaloSimpleSecondaryVertexNegativeHighEffBJetTags +
            akPu3CaloSimpleSecondaryVertexNegativeHighPurBJetTags +
            akPu3CaloCombinedSecondaryVertexNegativeBJetTags +
            akPu3CaloCombinedSecondaryVertexPositiveBJetTags
            )
        )


akPu3CaloJetBtaggingMu = cms.Sequence(akPu3CaloSoftMuonTagInfos * (akPu3CaloSoftMuonBJetTags +
    akPu3CaloSoftMuonByIP3dBJetTags +
    akPu3CaloSoftMuonByPtBJetTags +
    akPu3CaloNegativeSoftMuonByPtBJetTags +
    akPu3CaloPositiveSoftMuonByPtBJetTags
    )
    )

akPu3CaloJetBtagging = cms.Sequence(akPu3CaloJetBtaggingIP
        *akPu3CaloJetBtaggingSV
        *akPu3CaloJetBtaggingNegSV
        *akPu3CaloJetBtaggingMu
        )

#__________________________________________________________
# ----- flavour bit
akPu3CaloPatJetPartonAssociation       = patJetPartonAssociation.clone(jets    = cms.InputTag("akPu3CaloJets"),
        partons = cms.InputTag("genPartons"),
        coneSizeToAssociate = cms.double(0.4))
akPu3CaloPatJetFlavourAssociation      = patJetFlavourAssociation.clone(srcByReference = cms.InputTag("akPu3CaloPatJetPartonAssociation"))

akPu3CaloPatJetFlavourId               = cms.Sequence(akPu3CaloPatJetPartonAssociation*akPu3CaloPatJetFlavourAssociation)
#
#-------
#akPu3Calocorr = patJetCorrFactors.clone(src     = cms.InputTag("akPu3CaloJets"),
#        levels  = cms.vstring('L2Relative','L3Absolute'),
#        payload = cms.string('AK3PFTowers_hiGoodTightTracks')
#        )
akPu3Calomatch   = patJetGenJetMatch.clone(src      = cms.InputTag("akPu3CaloJets"),
        matched  = cms.InputTag("ak3clean"))
akPu3Caloparton  = patJetPartonMatch.clone(src      = cms.InputTag("akPu3CaloJets"))
akPu3CalopatJets = patJets.clone(jetSource            = cms.InputTag("akPu3CaloJets"),
        genJetMatch          = cms.InputTag("akPu3Calomatch"),
        genPartonMatch       = cms.InputTag("akPu3Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPu3CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu3CaloJetTracksAssociatorAtVertex"),
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu3CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu3CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu3CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu3CaloCombinedSecondaryVertexMVABJetTags"),
            cms.InputTag("akPu3CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPu3CaloJetProbabilityBJetTags"),
            cms.InputTag("akPu3CaloSoftMuonByPtBJetTags"),
            cms.InputTag("akPu3CaloSoftMuonByIP3dBJetTags"),
            cms.InputTag("akPu3CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu3CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu3CaloJetID"),
        )


  ###############################################################################

  #
  #
  # === data sequences ===
# Note still need to use enableData function in cfg to remove mc dep of patjet

# All corrections

#akPu1PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu1PFJets"),payload = cms.string('AKPu1PF_generalTracks'))
#akPu2PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu2PFJets"),payload = cms.string('AKPu2PF_generalTracks'))
akPu3PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets"),payload = cms.string('AKPu3PF_generalTracks'))
akPu4PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu4PFJets"),payload = cms.string('AKPu4PF_generalTracks'))
akPu5PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu5PFJets"),payload = cms.string('AKPu5PF_generalTracks'))
#akPu6PFcorr = akPu3PFcorr.clone(src = cms.InputTag("akPu6PFJets"),payload = cms.string('AKPu6PF_generalTracks'))

#ak1PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak1PFJets"),payload = cms.string('AK1PF_generalTracks'))
#ak2PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak2PFJets"),payload = cms.string('AK2PF_generalTracks'))
ak3PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak3PFJets"),payload = cms.string('AK3PF_generalTracks'))
ak4PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak4PFJets"),payload = cms.string('AK4PF_generalTracks'))
ak5PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak5PFJets"),payload = cms.string('AK5PF_generalTracks'))
#ak6PFcorr = akPu3PFcorr.clone(src = cms.InputTag("ak6PFJets"),payload = cms.string('AK6PF_generalTracks'))

#akPu1Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu1CaloJets"),payload = cms.string('AKPu1Calo_HI'))
#akPu2Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu2CaloJets"),payload = cms.string('AKPu2Calo_HI'))
akPu3Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu3CaloJets"),payload = cms.string('AKPu3Calo_HI'))
akPu4Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu4CaloJets"),payload = cms.string('AKPu4Calo_HI'))
akPu5Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu5CaloJets"),payload = cms.string('AKPu5Calo_HI'))
# We don't have corrections for ak6calo. This algorithm will be kept for debugging
#akPu6Calocorr = akPu3PFcorr.clone(src = cms.InputTag("akPu6CaloJets"),payload = cms.string('AKPu5Calo_HI'))

#ak1Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak1CaloJets"),payload = cms.string('AK1Calo_HI'))
#ak2Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak2CaloJets"),payload = cms.string('AK2Calo_HI'))
ak3Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak3CaloJets"),payload = cms.string('AK3Calo_HI'))
ak4Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak4CaloJets"),payload = cms.string('AK4Calo_HI'))
ak5Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak5CaloJets"),payload = cms.string('AK5Calo_HI'))
# We don't have corrections for ak6calo. This algorithm will be kept for debugging
#ak6Calocorr = akPu3PFcorr.clone(src = cms.InputTag("ak6CaloJets"),payload = cms.string('AK5Calo_HI'))

# Gen stuff

#ak1clean = akPu3PFclean.clone(src = cms.InputTag("ak1HiGenJets"))
#ak2clean = akPu3PFclean.clone(src = cms.InputTag("ak2HiGenJets"))
ak3clean = akPu3PFclean.clone(src = cms.InputTag("ak3HiGenJets"))
ak4clean = akPu3PFclean.clone(src = cms.InputTag("ak4HiGenJets"))
ak5clean = akPu3PFclean.clone(src = cms.InputTag("ak5HiGenJets"))
#ak6clean = akPu3PFclean.clone(src = cms.InputTag("ak6HiGenJets"))


#akPu1PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu1PFJets"), matched = cms.InputTag("ak1clean"))
#akPu2PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu2PFJets"), matched = cms.InputTag("ak2clean"))
akPu3PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets"), matched = cms.InputTag("ak3clean"))
akPu4PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu4PFJets"), matched = cms.InputTag("ak4clean"))
akPu5PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu5PFJets"), matched = cms.InputTag("ak5clean"))
#akPu6PFmatch = akPu3PFmatch.clone(src = cms.InputTag("akPu6PFJets"), matched = cms.InputTag("ak6clean"))

#akPu1Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu1CaloJets"), matched = cms.InputTag("ak1clean"))
#akPu2Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu2CaloJets"), matched = cms.InputTag("ak2clean"))
akPu3Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu3CaloJets"), matched = cms.InputTag("ak3clean"))
akPu4Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu4CaloJets"), matched = cms.InputTag("ak4clean"))
akPu5Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu5CaloJets"), matched = cms.InputTag("ak5clean"))
#akPu6Calomatch = akPu3PFmatch.clone(src = cms.InputTag("akPu6CaloJets"), matched = cms.InputTag("ak6clean"))

#ak1PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak1PFJets"), matched = cms.InputTag("ak1clean"))
#ak2PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak2PFJets"), matched = cms.InputTag("ak2clean"))
ak3PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak3PFJets"), matched = cms.InputTag("ak3clean"))
ak4PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak4PFJets"), matched = cms.InputTag("ak4clean"))
ak5PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak5PFJets"), matched = cms.InputTag("ak5clean"))
#ak6PFmatch = akPu3PFmatch.clone(src = cms.InputTag("ak6PFJets"), matched = cms.InputTag("ak6clean"))

#ak1Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak1CaloJets"), matched = cms.InputTag("ak1clean"))
#ak2Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak2CaloJets"), matched = cms.InputTag("ak2clean"))
ak3Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak3CaloJets"), matched = cms.InputTag("ak3clean"))
ak4Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak4CaloJets"), matched = cms.InputTag("ak4clean"))
ak5Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak5CaloJets"), matched = cms.InputTag("ak5clean"))
#ak6Calomatch = akPu3PFmatch.clone(src = cms.InputTag("ak6CaloJets"), matched = cms.InputTag("ak6clean"))

#akPu1PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu1PFJets"))
#akPu2PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu2PFJets"))
akPu3PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets"))
akPu4PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu4PFJets"))
akPu5PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu5PFJets"))
#akPu6PFparton = akPu3PFparton.clone(src = cms.InputTag("akPu6PFJets"))

#akPu1Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu1CaloJets"))
#akPu2Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu2CaloJets"))
akPu3Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu3CaloJets"))
akPu4Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu4CaloJets"))
akPu5Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu5CaloJets"))
#akPu6Caloparton = akPu3PFparton.clone(src = cms.InputTag("akPu6CaloJets"))
#ak1PFparton = akPu3PFparton.clone(src = cms.InputTag("ak1PFJets"))
#ak2PFparton = akPu3PFparton.clone(src = cms.InputTag("ak2PFJets"))
ak3PFparton = akPu3PFparton.clone(src = cms.InputTag("ak3PFJets"))
ak4PFparton = akPu3PFparton.clone(src = cms.InputTag("ak4PFJets"))
ak5PFparton = akPu3PFparton.clone(src = cms.InputTag("ak5PFJets"))
#ak6PFparton = akPu3PFparton.clone(src = cms.InputTag("ak6PFJets"))
#ak1Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak1CaloJets"))
#ak2Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak2CaloJets"))
ak3Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak3CaloJets"))
ak4Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak4CaloJets"))
ak5Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak5CaloJets"))
#ak6Caloparton = akPu3PFparton.clone(src = cms.InputTag("ak6CaloJets"))


# PAT Maker

#akPu1PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu1PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu1PFcorr")), genJetMatch = cms.InputTag("akPu1PFmatch"), genPartonMatch = cms.InputTag("akPu1PFparton"),jetIDMap = cms.InputTag("akPu1PFJetID"))
#akPu2PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr")), genJetMatch = cms.InputTag("akPu2PFmatch"), genPartonMatch = cms.InputTag("akPu2PFparton"),jetIDMap = cms.InputTag("akPu2PFJetID"))
#akPu3PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr")), genJetMatch = cms.InputTag("akPu3PFmatch"), genPartonMatch = cms.InputTag("akPu3PFparton"),jetIDMap = cms.InputTag("akPu3PFJetID"))
#akPu4PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr")), genJetMatch = cms.InputTag("akPu4PFmatch"), genPartonMatch = cms.InputTag("akPu4PFparton"),jetIDMap = cms.InputTag("akPu4PFJetID"))
#akPu5PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu5PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5PFcorr")), genJetMatch = cms.InputTag("akPu5PFmatch"), genPartonMatch = cms.InputTag("akPu5PFparton"),jetIDMap = cms.InputTag("akPu5PFJetID"))
#akPu6PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu6PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6PFcorr")), genJetMatch = cms.InputTag("akPu6PFmatch"), genPartonMatch = cms.InputTag("akPu6PFparton"),jetIDMap = cms.InputTag("akPu6PFJetID"))
#akPu1CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu1CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu1Calocorr")), genJetMatch = cms.InputTag("akPu1Calomatch"), genPartonMatch = cms.InputTag("akPu1Caloparton"),jetIDMap = cms.InputTag("akPu1CaloJetID"))
#akPu2CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu2CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr")), genJetMatch = cms.InputTag("akPu2Calomatch"), genPartonMatch = cms.InputTag("akPu2Caloparton"),jetIDMap = cms.InputTag("akPu2CaloJetID"))
#akPu3CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr")), genJetMatch = cms.InputTag("akPu3Calomatch"), genPartonMatch = cms.InputTag("akPu3Caloparton"),jetIDMap = cms.InputTag("akPu3CaloJetID"))
#akPu4CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu4CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr")), genJetMatch = cms.InputTag("akPu4Calomatch"), genPartonMatch = cms.InputTag("akPu4Caloparton"),jetIDMap = cms.InputTag("akPu4CaloJetID"))
#akPu5CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu5CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5Calocorr")), genJetMatch = cms.InputTag("akPu5Calomatch"), genPartonMatch = cms.InputTag("akPu5Caloparton"),jetIDMap = cms.InputTag("akPu5CaloJetID"))
#akPu6CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu6CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu6Calocorr")), genJetMatch = cms.InputTag("akPu6Calomatch"), genPartonMatch = cms.InputTag("akPu6Caloparton"),jetIDMap = cms.InputTag("akPu6CaloJetID"))
#ak1PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak1PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak1PFcorr")), genJetMatch = cms.InputTag("ak1PFmatch"), genPartonMatch = cms.InputTag("ak1PFparton"),jetIDMap = cms.InputTag("ak1PFJetID"))
#ak2PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak2PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak2PFcorr")), genJetMatch = cms.InputTag("ak2PFmatch"), genPartonMatch = cms.InputTag("ak2PFparton"),jetIDMap = cms.InputTag("ak2PFJetID"))
#ak3PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak3PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3PFcorr")), genJetMatch = cms.InputTag("ak3PFmatch"), genPartonMatch = cms.InputTag("ak3PFparton"),jetIDMap = cms.InputTag("ak3PFJetID"))
#ak4PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak4PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4PFcorr")), genJetMatch = cms.InputTag("ak4PFmatch"), genPartonMatch = cms.InputTag("ak4PFparton"),jetIDMap = cms.InputTag("ak4PFJetID"))
#ak5PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak5PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5PFcorr")), genJetMatch = cms.InputTag("ak5PFmatch"), genPartonMatch = cms.InputTag("ak5PFparton"),jetIDMap = cms.InputTag("ak5PFJetID"))
#ak6PFpatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak6PFJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak6PFcorr")), genJetMatch = cms.InputTag("ak6PFmatch"), genPartonMatch = cms.InputTag("ak6PFparton"),jetIDMap = cms.InputTag("ak6PFJetID"))
#ak1CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak1CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak1Calocorr")), genJetMatch = cms.InputTag("ak1Calomatch"), genPartonMatch = cms.InputTag("ak1Caloparton"),jetIDMap = cms.InputTag("ak1CaloJetID"))
#ak2CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak2CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak2Calocorr")), genJetMatch = cms.InputTag("ak2Calomatch"), genPartonMatch = cms.InputTag("ak2Caloparton"),jetIDMap = cms.InputTag("ak2CaloJetID"))
#ak3CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak3CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3Calocorr")), genJetMatch = cms.InputTag("ak3Calomatch"), genPartonMatch = cms.InputTag("ak3Caloparton"),jetIDMap = cms.InputTag("ak3CaloJetID"))
#ak4CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak4CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4Calocorr")), genJetMatch = cms.InputTag("ak4Calomatch"), genPartonMatch = cms.InputTag("ak4Caloparton"),jetIDMap = cms.InputTag("ak4CaloJetID"))
#ak5CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak5CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5Calocorr")), genJetMatch = cms.InputTag("ak5Calomatch"), genPartonMatch = cms.InputTag("ak5Caloparton"),jetIDMap = cms.InputTag("ak5CaloJetID"))
#ak6CalopatJets = akPu3PFpatJets.clone(jetSource = cms.InputTag("ak6CaloJets"), jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak6Calocorr")), genJetMatch = cms.InputTag("ak6Calomatch"), genPartonMatch = cms.InputTag("ak6Caloparton"),jetIDMap = cms.InputTag("ak6CaloJetID"))

icPu5patSequence = cms.Sequence(icPu5corr * icPu5clean * icPu5match * icPu5parton  *  icPu5patJets)

#akPu1PFpatSequence = cms.Sequence(akPu1PFcorr+ak1clean+akPu1PFmatch+akPu1PFparton+akPu1PFpatJets)
#akPu2PFpatSequence = cms.Sequence(akPu2PFcorr+ak2clean+akPu2PFmatch+akPu2PFparton+akPu2PFpatJets)
akPu3PFpatSequence = cms.Sequence(akPu3PFcorr+ak3clean+akPu3PFmatch+akPu3PFparton+akPu3PFpatJets)
akPu4PFpatSequence = cms.Sequence(akPu4PFcorr+ak4clean+akPu4PFmatch+akPu4PFparton+akPu4PFpatJets)
akPu5PFpatSequence = cms.Sequence(akPu5PFcorr+ak5clean+akPu5PFmatch+akPu5PFparton+akPu5PFpatJets)
#akPu6PFpatSequence = cms.Sequence(akPu6PFcorr+ak6clean+akPu6PFmatch+akPu6PFparton+akPu6PFpatJets)

#akPu1CalopatSequence = cms.Sequence(akPu1Calocorr+ak1clean+akPu1Calomatch+akPu1Caloparton+akPu1CalopatJets)
#akPu2CalopatSequence = cms.Sequence(akPu2Calocorr+ak2clean+akPu2Calomatch+akPu2Caloparton+akPu2CalopatJets)
akPu3CalopatSequence = cms.Sequence(akPu3Calocorr+ak3clean+akPu3Calomatch+akPu3Caloparton+akPu3CalopatJets)
akPu4CalopatSequence = cms.Sequence(akPu4Calocorr+ak4clean+akPu4Calomatch+akPu4Caloparton+akPu4CalopatJets)
akPu5CalopatSequence = cms.Sequence(akPu5Calocorr+ak5clean+akPu5Calomatch+akPu5Caloparton+akPu5CalopatJets)
#akPu6CalopatSequence = cms.Sequence(akPu6Calocorr+ak6clean+akPu6Calomatch+akPu6Caloparton+akPu6CalopatJets)

#ak1PFpatSequence = cms.Sequence(ak1PFcorr+ak1clean+ak1PFmatch+ak1PFparton+ak1PFpatJets)
#ak2PFpatSequence = cms.Sequence(ak2PFcorr+ak2clean+ak2PFmatch+ak2PFparton+ak2PFpatJets)
ak3PFpatSequence = cms.Sequence(ak3PFcorr+ak3clean+ak3PFmatch+ak3PFparton+ak3PFpatJets)
ak4PFpatSequence = cms.Sequence(ak4PFcorr+ak4clean+ak4PFmatch+ak4PFparton+ak4PFpatJets)
ak5PFpatSequence = cms.Sequence(ak5PFcorr+ak5clean+ak5PFmatch+ak5PFparton+ak5PFpatJets)
#ak6PFpatSequence = cms.Sequence(ak6PFcorr+ak6clean+ak6PFmatch+ak6PFparton+ak6PFpatJets)

#ak1CalopatSequence = cms.Sequence(ak1Calocorr+ak1clean+ak1Calomatch+ak1Caloparton+ak1CalopatJets)
#ak2CalopatSequence = cms.Sequence(ak2Calocorr+ak2clean+ak2Calomatch+ak2Caloparton+ak2CalopatJets)
ak3CalopatSequence = cms.Sequence(ak3Calocorr+ak3clean+ak3Calomatch+ak3Caloparton+ak3CalopatJets)
ak4CalopatSequence = cms.Sequence(ak4Calocorr+ak4clean+ak4Calomatch+ak4Caloparton+ak4CalopatJets)
ak5CalopatSequence = cms.Sequence(ak5Calocorr+ak5clean+ak5Calomatch+ak5Caloparton+ak5CalopatJets)
#ak6CalopatSequence = cms.Sequence(ak6Calocorr+ak6clean+ak6Calomatch+ak6Caloparton+ak6CalopatJets)

#<<<<<<< PatAna_MC_cff.py
akPu3PFpatSequence_withBtagging = cms.Sequence(akPu3PFcorr * ak3clean * akPu3PFmatch * akPu3PFparton * akPu3PFPatJetFlavourId * akPu3PFJetTracksAssociator * akPu3PFJetBtagging * akPu3PFpatJets)
akPu4PFpatSequence_withBtagging = cms.Sequence(akPu4PFcorr * ak4clean * akPu4PFmatch * akPu4PFparton * akPu4PFPatJetFlavourId * akPu4PFJetTracksAssociator * akPu4PFJetBtagging * akPu4PFpatJets)
akPu5PFpatSequence_withBtagging = cms.Sequence(akPu5PFcorr * ak5clean * akPu5PFmatch * akPu5PFparton * akPu5PFPatJetFlavourId * akPu5PFJetTracksAssociator * akPu5PFJetBtagging * akPu5PFpatJets)

ak3PFpatSequence_withBtagging = cms.Sequence(ak3PFcorr * ak3clean * ak3PFmatch * ak3PFparton * ak3PFPatJetFlavourId * ak3PFJetTracksAssociator * ak3PFJetBtagging * ak3PFpatJets)
ak4PFpatSequence_withBtagging = cms.Sequence(ak4PFcorr * ak4clean * ak4PFmatch * ak4PFparton * ak4PFPatJetFlavourId * ak4PFJetTracksAssociator * ak4PFJetBtagging * ak4PFpatJets)
ak5PFpatSequence_withBtagging = cms.Sequence(ak5PFcorr * ak5clean * ak5PFmatch * ak5PFparton * ak5PFPatJetFlavourId * ak5PFJetTracksAssociator * ak5PFJetBtagging * ak5PFpatJets)

akPu3CalopatSequence_withBtagging = cms.Sequence(akPu3Calocorr * ak3clean * akPu3Calomatch * akPu3Caloparton * akPu3CaloPatJetFlavourId * akPu3CaloJetTracksAssociator * akPu3CaloJetBtagging * akPu3CalopatJets)
akPu4CalopatSequence_withBtagging = cms.Sequence(akPu4Calocorr * ak4clean * akPu4Calomatch * akPu4Caloparton * akPu4CaloPatJetFlavourId * akPu4CaloJetTracksAssociator * akPu4CaloJetBtagging * akPu4CalopatJets)
akPu5CalopatSequence_withBtagging = cms.Sequence(akPu5Calocorr * ak5clean * akPu5Calomatch * akPu5Caloparton * akPu5CaloPatJetFlavourId * akPu5CaloJetTracksAssociator * akPu5CaloJetBtagging * akPu5CalopatJets)

ak3CalopatSequence_withBtagging = cms.Sequence(ak3Calocorr * ak3clean * ak3Calomatch * ak3Caloparton * ak3CaloPatJetFlavourId * ak3CaloJetTracksAssociator * ak3CaloJetBtagging * ak3CalopatJets)
ak4CalopatSequence_withBtagging = cms.Sequence(ak4Calocorr * ak4clean * ak4Calomatch * ak4Caloparton * ak4CaloPatJetFlavourId * ak4CaloJetTracksAssociator * ak4CaloJetBtagging * ak4CalopatJets)
ak5CalopatSequence_withBtagging = cms.Sequence(ak5Calocorr * ak5clean * ak5Calomatch * ak5Caloparton * ak5CaloPatJetFlavourId * ak5CaloJetTracksAssociator * ak5CaloJetBtagging * ak5CalopatJets)


makeHeavyIonJets = cms.Sequence(
#                                akPu1PFpatSequence +
#                                akPu2PFpatSequence +
                                akPu3PFpatSequence_withBtagging +
#                                akPu4PFpatSequence +
                                akPu5PFpatSequence_withBtagging 
#                                akPu6PFpatSequence +

#                                akPu1CalopatSequence +
#                                akPu2CalopatSequence +
#                                akPu3CalopatSequence +
#                                akPu4CalopatSequence +
#                                akPu5CalopatSequence +
                                
                                )

makeHeavyIonJets3to5 = cms.Sequence(
#                                akPu2PFpatSequence +
                                akPu3PFpatSequence_withBtagging +
                                akPu4PFpatSequence_withBtagging +
                                akPu5PFpatSequence_withBtagging + 

 #                               akPu2CalopatSequence +
                                akPu3CalopatSequence_withBtagging +
                                akPu4CalopatSequence_withBtagging +
                                 akPu5CalopatSequence_withBtagging + 
                                
 #                               ak2PFpatSequence +
                                ak3PFpatSequence_withBtagging +
                                ak4PFpatSequence_withBtagging +
                                ak5PFpatSequence_withBtagging + 
                                
 #                               ak2CalopatSequence +
                                ak3CalopatSequence_withBtagging +
                                ak4CalopatSequence_withBtagging +
                                ak5CalopatSequence_withBtagging 
                                
                                )
                               
