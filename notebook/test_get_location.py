import liegecolloquium
import unittest

class TestMeshMethods(unittest.TestCase):

    def setUp(self):
        self.l1 = ['Abbot', 'M.B.', 'Delft University', 'Delft', 'The Netherlands']
        self.l2 = ['Abbot', 'M.B.', 'Delff University', 'Defff', 'The Netvrherlands']

    def test_existing_affiliation(self):
        """
        Get location using a correct address
        """
        participant = liegecolloquium.Participant(self.l1[0], self.l1[1], self.l1[2],
                                                  self.l1[3], self.l1[4])
        participant.get_location()
        self.assertEqual(participant.lon, 4.37392311388339)
        self.assertEqual(participant.lat, 51.9988187)

    def test_wrong_address(self):
        """
        Get location using a mispelled address
        """
        participant = liegecolloquium.Participant(self.l2[0], self.l2[1],
                                                  self.l2[2], self.l2[3],
                                                  self.l2[4])

        participant.get_location()
        self.assertEqual(participant.lon, 52.023430000000076)
        self.assertEqual(participant.lat, 4.352890000000059)