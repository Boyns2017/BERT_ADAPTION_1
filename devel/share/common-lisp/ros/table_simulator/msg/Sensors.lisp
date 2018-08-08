; Auto-generated. Do not edit!


(cl:in-package table_simulator-msg)


;//! \htmlinclude Sensors.msg.html

(cl:defclass <Sensors> (roslisp-msg-protocol:ros-message)
  ((gaze
    :reader gaze
    :initarg :gaze
    :type cl:float
    :initform 0.0)
   (location
    :reader location
    :initarg :location
    :type cl:float
    :initform 0.0)
   (pressure
    :reader pressure
    :initarg :pressure
    :type cl:float
    :initform 0.0))
)

(cl:defclass Sensors (<Sensors>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Sensors>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Sensors)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name table_simulator-msg:<Sensors> is deprecated: use table_simulator-msg:Sensors instead.")))

(cl:ensure-generic-function 'gaze-val :lambda-list '(m))
(cl:defmethod gaze-val ((m <Sensors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:gaze-val is deprecated.  Use table_simulator-msg:gaze instead.")
  (gaze m))

(cl:ensure-generic-function 'location-val :lambda-list '(m))
(cl:defmethod location-val ((m <Sensors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:location-val is deprecated.  Use table_simulator-msg:location instead.")
  (location m))

(cl:ensure-generic-function 'pressure-val :lambda-list '(m))
(cl:defmethod pressure-val ((m <Sensors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:pressure-val is deprecated.  Use table_simulator-msg:pressure instead.")
  (pressure m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Sensors>) ostream)
  "Serializes a message object of type '<Sensors>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'gaze))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'location))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pressure))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Sensors>) istream)
  "Deserializes a message object of type '<Sensors>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'gaze) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'location) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pressure) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Sensors>)))
  "Returns string type for a message object of type '<Sensors>"
  "table_simulator/Sensors")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Sensors)))
  "Returns string type for a message object of type 'Sensors"
  "table_simulator/Sensors")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Sensors>)))
  "Returns md5sum for a message object of type '<Sensors>"
  "d86d90edfb309afce5a122c5fd284811")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Sensors)))
  "Returns md5sum for a message object of type 'Sensors"
  "d86d90edfb309afce5a122c5fd284811")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Sensors>)))
  "Returns full string definition for message of type '<Sensors>"
  (cl:format cl:nil "float32 gaze~%float32 location~%float32 pressure~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Sensors)))
  "Returns full string definition for message of type 'Sensors"
  (cl:format cl:nil "float32 gaze~%float32 location~%float32 pressure~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Sensors>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Sensors>))
  "Converts a ROS message object to a list"
  (cl:list 'Sensors
    (cl:cons ':gaze (gaze msg))
    (cl:cons ':location (location msg))
    (cl:cons ':pressure (pressure msg))
))
